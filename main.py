import re
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="전국 인구구조 지도", layout="wide")

POP_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/population_yearly.csv.gz"
GEO_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/boundaries/sigungu_kr.geojson"

@st.cache_data(show_spinner="인구 데이터를 불러오는 중입니다...")
def load_population():
    return pd.read_csv(POP_URL, dtype={"코드": str})

@st.cache_data(show_spinner="지도 경계를 불러오는 중입니다...")
def load_geojson():
    return requests.get(GEO_URL, timeout=30).json()

df_raw = load_population()
geojson = load_geojson()

# ---------------------------------------------------------
# 사이드바 설정 (필터 및 연도 선택)
# ---------------------------------------------------------
st.sidebar.title("⚙️ 설정")

# 지표 선택
metric_type = st.sidebar.radio(
    "📊 분석 지표 선택",
    ["고령화율 (65세 이상)", "유소년 비율 (0~14세)"],
    index=0
)

# 연도 선택 슬라이더
min_year = int(df_raw["연도"].min())
max_year = int(df_raw["연도"].max())
selected_year = st.sidebar.slider(
    "📅 연도 선택",
    min_value=min_year,
    max_value=max_year,
    value=max_year,
    step=1
)

# ---------------------------------------------------------
# 데이터 전처리
# ---------------------------------------------------------
df = df_raw[df_raw["연도"] == selected_year].copy()

# '계_'로 시작하는 나이 열 필터링
total_cols = [c for c in df.columns if c.startswith("계_")]

def age_of(col):
    m = re.match(r"계_(\d+)세", col)
    return int(m.group(1)) if m else None

# 인구 그룹별 열 분류
elderly_cols = [c for c in total_cols if age_of(c) is not None and age_of(c) >= 65]
child_cols = [c for c in total_cols if age_of(c) is not None and age_of(c) <= 14]

df["전체인구"] = df[total_cols].sum(axis=1)
df["고령인구"] = df[elderly_cols].sum(axis=1)
df["유소년인구"] = df[child_cols].sum(axis=1)

# 시군구 코드 생성 및 행정구역 개편 보정
df["시군구코드"] = df["코드"].str[:5]

# 옛 코드 보정 (42->51, 45->52, 47720->27720)
def fix_sigungu_code(code):
    if code.startswith("42"):
        return "51" + code[2:]
    elif code.startswith("45"):
        return "52" + code[2:]
    elif code == "47720":
        return "27720"
    return code

df["시군구코드"] = df["시군구코드"].apply(fix_sigungu_code)

# 시군구별 집계
grouped = df.groupby("시군구코드")[["전체인구", "고령인구", "유소년인구"]].sum().reset_index()
grouped["고령화율"] = (grouped["고령인구"] / grouped["전체인구"] * 100).round(2)
grouped["유소년비율"] = (grouped["유소년인구"] / grouped["전체인구"] * 100).round(2)

# GeoJSON 매칭 정보 결합
names = pd.DataFrame([
    {
        "시군구코드": str(f["properties"]["코드"]),
        "시군구": f["properties"]["시군구"],
        "시도": f["properties"]["시도"],
    }
    for f in geojson["features"]
])

merged = grouped.merge(names, on="시군구코드", how="left")

# ---------------------------------------------------------
# 시도 필터링
# ---------------------------------------------------------
sido_list = ["전국"] + sorted(list(names["시도"].unique()))
selected_sido = st.sidebar.selectbox("🗺️ 지역 선택 (시도)", sido_list)

# 지표별 구체 설정 (구간, 색상, 레이블)
if metric_type == "고령화율 (65세 이상)":
    target_col = "고령화율"
    bins = [0, 19, 23, 28, 38, 100]
    labels = ["19% 미만", "19~23%", "23~28%", "28~38%", "38% 이상"]
    color_map = {
        "19% 미만": "#fee6ce",
        "19~23%": "#fdc086",
        "23~28%": "#f79646",
        "28~38%": "#e8590c",
        "38% 이상": "#a63603",
    }
    legend_title = f"65세 이상 비율 ({selected_year}년)"
    unit_suffix = "%"
else:
    target_col = "유소년비율"
    bins = [0, 8, 10, 12, 14, 100]
    labels = ["8% 미만", "8~10%", "10~12%", "12~14%", "14% 이상"]
    color_map = {
        "8% 미만": "#eff3ff",
        "8~10%": "#bdd7e7",
        "10~12%": "#6baed6",
        "12~14%": "#3182bd",
        "14% 이상": "#08519c",
    }
    legend_title = f"0~14세 비율 ({selected_year}년)"
    unit_suffix = "%"

merged["단계"] = pd.cut(merged[target_col], bins=bins, labels=labels, right=False)

# 선택된 시도 필터링 적용 (지도 뷰어용)
if selected_sido != "전국":
    display_merged = merged[merged["시도"] == selected_sido]
    filtered_geojson = {
        "type": "FeatureCollection",
        "features": [
            f for f in geojson["features"] if f["properties"]["시도"] == selected_sido
        ]
    }
else:
    display_merged = merged
    filtered_geojson = geojson

# ---------------------------------------------------------
# 대시보드 UI 출력
# ---------------------------------------------------------
st.title(f"🗺️ 전국 {metric_type.split(' ')[0]} 지도")
st.caption(f"행정안전부 주민등록 인구 기준 ({selected_year}년 데이터)")

# 상단 KPI 카드
nat_total_pop = merged["전체인구"].sum()
if metric_type == "고령화율 (65세 이상)":
    nat_target_pop = merged["고령인구"].sum()
else:
    nat_target_pop = merged["유소년인구"].sum()

national_rate = round((nat_target_pop / nat_total_pop) * 100, 2)

valid_data = merged.dropna(subset=["시군구"])
max_row = valid_data.loc[valid_data[target_col].idxmax()]
min_row = valid_data.loc[valid_data[target_col].idxmin()]

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("전국 평균", f"{national_rate}{unit_suffix}")
kpi2.metric(f"가장 높은 곳", f"{max_row['시도']} {max_row['시군구']}", f"{max_row[target_col]}{unit_suffix}")
kpi3.metric(f"가장 낮은 곳", f"{min_row['시도']} {min_row['시군구']}", f"{min_row[target_col]}{unit_suffix}")

st.divider()

# 지도 시각화
fig = px.choropleth(
    display_merged,
    geojson=filtered_geojson,
    locations="시군구코드",
    featureidkey="properties.코드",
    color="단계",
    category_orders={"단계": labels},
    color_discrete_map=color_map,
    hover_name="시군구",
    hover_data={target_col: True, "시도": True, "시군구코드": False, "단계": False},
    labels={target_col: f"{metric_type.split(' ')[0]} (%)"},
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    height=650,
    legend_title_text=legend_title,
)

st.plotly_chart(fig, use_container_width=True)

# 안 맞는 행정구역 안내 메시지
unmapped_count = merged["시군구"].isna().sum()
if unmapped_count > 0:
    st.info(f"💡 현재 연도 기준 경계 파일 데이터와 매칭되지 않는 과거/신규 행정구역이 {unmapped_count}개 존재합니다. (지도상 회색 처리)")

st.divider()

# 지도 하단 순위 표
c1, c2 = st.columns(2)
cols = ["시도", "시군구", target_col]

with c1:
    st.subheader(f"🔴 {metric_type.split(' ')[0]} 높은 곳 TOP 10")
    st.dataframe(
        valid_data.nlargest(10, target_col)[cols].reset_index(drop=True),
        use_container_width=True
    )
with c2:
    st.subheader(f"🟢 {metric_type.split(' ')[0]} 낮은 곳 TOP 10")
    st.dataframe(
        valid_data.nsmallest(10, target_col)[cols].reset_index(drop=True),
        use_container_width=True
    )
