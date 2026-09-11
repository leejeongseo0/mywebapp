
        labels[2]: 3,
        labels[3]: 4,
        labels[4]: 5,
    }

    fig.add_trace(
        go.Choropleth(
            geojson=map_geojson,
            locations=subset["시군구코드"],
            z=[
                code_to_number[label]
                for _ in range(len(subset))
            ],
            featureidkey="properties.코드",
            colorscale=[
                [0, colors[label]],
                [1, colors[label]],
            ],
            showscale=False,
            name=label,
            marker_line_color="white",
            marker_line_width=0.7,
            customdata=subset[
                [
                    "시군구",
                    "시도",
                    "지표값",
                ]
            ].values,
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "시도: %{customdata[1]}<br>"
                f"{legend_title}: "
                "%{customdata[2]:.2f}%"
                "<extra></extra>"
            ),
        )
    )


# ------------------------------------------------------------
# 지도 화면 설정
# ------------------------------------------------------------

fig.update_geos(
    fitbounds="locations",
    visible=False,
)


fig.update_layout(
    margin=dict(
        l=0,
        r=0,
        t=10,
        b=0,
    ),
    height=700,
    paper_bgcolor="rgba(0,0,0,0)",
    geo=dict(
        bgcolor="rgba(0,0,0,0)",
    ),
    legend=dict(
        title=f"{legend_title} · {selected_year}년",
        orientation="v",
        yanchor="top",
        y=0.98,
        xanchor="left",
        x=0.01,
    ),
)


st.plotly_chart(
    fig,
    use_container_width=True,
)


# ============================================================
# 안내 문구
# ============================================================

# 데이터가 존재하지만 현재 경계 파일에서 이름을 찾지 못한 지역
unmatched = merged[
    merged["시군구"].isna()
].copy()


if len(unmatched) > 0:

    st.warning(
        "⚠️ 일부 과거 행정구역 코드는 현재 경계 파일과 "
        "일치하지 않아 지도에서 회색으로 표시될 수 있습니다. "
        "강원(42→51), 전북(45→52), 군위군(47720→27720)은 "
        "코드를 보정했으며, 그래도 일치하지 않는 지역은 "
        "회색으로 표시했습니다."
    )


# ============================================================
# 지도 아래 순위표
# ============================================================

st.markdown("---")

table_title = (
    f"📋 {selected_year}년 "
    f"{selected_sido} {legend_title} 순위"
)

st.subheader(table_title)


table_cols = [
    "시도",
    "시군구",
    "지표값",
]


ranked = (
    map_df[
        map_df["지표값"].notna()
    ][table_cols]
    .sort_values(
        "지표값",
        ascending=False,
    )
    .reset_index(drop=True)
)


c1, c2 = st.columns(2)


with c1:

    st.markdown("#### 🔴 높은 곳 TOP 10")

    high_table = ranked.head(10).copy()

    high_table["지표값"] = (
        high_table["지표값"]
        .map(lambda x: f"{x:.2f}%")
    )

    high_table.columns = [
        "시도",
        "시군구",
        "비율",
    ]

    st.dataframe(
        high_table,
        use_container_width=True,
        hide_index=True,
    )


with c2:

    st.markdown("#### 🟢 낮은 곳 TOP 10")

    low_table = ranked.tail(10).sort_values(
        "지표값",
        ascending=True,
    ).copy()

    low_table["지표값"] = (
        low_table["지표값"]
        .map(lambda x: f"{x:.2f}%")
    )

    low_table.columns = [
        "시도",
        "시군구",
        "비율",
    ]

    st.dataframe(
        low_table,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# 하단 설명
# ============================================================

st.caption(
    "※ 지도 색 구간은 연도가 바뀌어도 동일하게 유지됩니다. "
    "따라서 서로 다른 연도의 색 분포를 직접 비교할 수 있습니다."
)

if indicator == "0~14세 유소년인구 비율":

    st.caption(
        "※ 유소년인구 비율의 색 구간은 고령인구와 별도로 "
        "설정되어 있습니다. 유소년 비율의 상대적으로 작은 "
        "범위를 구분하여 지도에서 차이가 보이도록 했습니다."
    )
