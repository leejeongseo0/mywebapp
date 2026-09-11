from pathlib import Path

app = r'''import streamlit as st

st.set_page_config(
    page_title="MBTI 여행 콕콕 💗",
    page_icon="🌷",
    layout="centered",
)

# ---------- Theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}
.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffe9f2 0, transparent 28%),
        radial-gradient(circle at 90% 20%, #e7f4ff 0, transparent 28%),
        linear-gradient(180deg, #fffafd 0%, #f8fbff 100%);
}
h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
    color: #5b4b63;
}
.hero {
    text-align: center;
    padding: 28px 18px 20px;
    background: rgba(255,255,255,.72);
    border: 2px solid #ffdce9;
    border-radius: 28px;
    box-shadow: 0 12px 35px rgba(115, 82, 110, .10);
}
.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: 2.65rem;
    color: #ff6f9d;
    margin: 0;
}
.hero-sub {
    color: #7a6d80;
    font-size: 1.05rem;
    margin-top: 8px;
}
.badge {
    display: inline-block;
    padding: 7px 14px;
    margin: 5px;
    border-radius: 999px;
    background: #fff0f6;
    color: #e95f8f;
    font-weight: 800;
}
.place-card {
    background: white;
    border: 2px solid #f2e5ee;
    border-radius: 24px;
    padding: 20px;
    margin: 12px 0;
    box-shadow: 0 8px 22px rgba(100,80,110,.08);
}
.place-name {
    font-family: 'Jua', sans-serif;
    font-size: 1.65rem;
    color: #63536c;
}
.reason {
    color: #756878;
    line-height: 1.65;
}
.tip {
    background: #fff7d9;
    border-radius: 16px;
    padding: 12px 15px;
    color: #78652d;
    margin-top: 10px;
}
.stButton > button {
    border-radius: 18px;
    border: 2px solid #ffd1e1;
    background: linear-gradient(135deg, #fff, #fff0f6);
    color: #d95687;
    font-weight: 800;
}
div[data-testid="stSelectbox"] label {
    font-weight: 800;
    color: #66566d;
}
.footer {
    text-align: center;
    color: #9a8d9f;
    font-size: .9rem;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Data ----------
destinations = {
    "INFP": [
        ("🌿 교토", "일본", "조용한 골목과 사찰, 계절 풍경 속에서 천천히 나만의 시간을 보내기 좋아요.", "아라시야마 산책 + 작은 카페 한 곳을 골라 여유롭게 즐겨봐요."),
        ("🌊 제주", "대한민국", "자연을 바라보며 생각을 정리하고 감성을 충전하기 딱 좋은 여행지예요.", "바다 산책 후 노을 명소에서 멍때리기 추천!"),
        ("🎨 파리", "프랑스", "예쁜 거리와 미술관, 작은 서점과 카페가 감성 레이더를 자극해요.", "유명 명소만 찍기보다 골목을 천천히 걸어보세요."),
    ],
    "INTP": [
        ("🔭 도쿄", "일본", "새로운 기술과 독특한 문화, 관심사를 마음껏 파고들 수 있는 도시예요.", "과학관·전자상가·서브컬처 공간처럼 취향 따라 코스를 바꿔보세요."),
        ("🏛️ 런던", "영국", "박물관과 과학·역사 콘텐츠가 풍부해서 혼자 탐험하기 좋아요.", "무료 박물관을 골라 관심 분야부터 깊게 파고들어 보세요."),
        ("🧪 싱가포르", "싱가포르", "미래 도시 풍경과 과학·자연이 조화돼 새로운 걸 발견하는 재미가 있어요.", "가든스 바이 더 베이와 과학 관련 공간을 함께 넣어보세요."),
    ],
    "ENFP": [
        ("🎡 런던", "영국", "볼거리도 많고 다양한 사람과 문화가 섞여 있어 즉흥적인 모험에 잘 어울려요.", "하루 한 곳은 계획 없이 골목에서 발견해보기!"),
        ("🌺 방콕", "태국", "맛있는 음식, 활기찬 거리, 색다른 문화가 가득해서 에너지가 팡팡 올라가요.", "시장과 야경 스폿을 넣으면 여행이 더 신나요."),
        ("🌈 오사카", "일본", "먹거리와 쇼핑, 재미있는 명소가 많아서 신나게 돌아다니기 좋아요.", "맛집 하나만 정하고 나머지는 현장에서 골라봐요."),
    ],
    "ENTP": [
        ("🏙️ 뉴욕", "미국", "끊임없이 새로운 아이디어와 사람을 만날 수 있어 지루할 틈이 없어요.", "동네 하나를 정해 예상 밖의 가게와 전시를 찾아보세요."),
        ("🚀 베를린", "독일", "개성 있는 문화와 실험적인 공간이 많아 호기심을 자극해요.", "박물관보다 독립적인 문화 공간을 찾아보는 것도 좋아요."),
        ("🎮 도쿄", "일본", "전통부터 최신 기술과 대중문화까지 서로 다른 세계를 한 도시에서 만날 수 있어요.", "하루에 서로 다른 분위기의 지역 2~3곳을 섞어보세요."),
    ],
    "ISFP": [
        ("🌸 후쿠오카", "일본", "맛있는 음식과 아늑한 골목, 바다까지 부담 없이 즐길 수 있어요.", "카페 한 곳 + 바닷가 산책처럼 느슨한 일정이 잘 맞아요."),
        ("🏝️ 다낭", "베트남", "아름다운 자연과 편안한 분위기에서 쉬면서 소소한 즐거움을 찾기 좋아요.", "일정을 빡빡하게 채우지 말고 휴식 시간을 꼭 남겨두세요."),
        ("🌿 제주", "대한민국", "자연과 맛집, 감성적인 공간을 내 취향대로 골라 즐길 수 있어요.", "사진 찍기 좋은 자연 명소 하나를 골라 천천히 즐겨보세요."),
    ],
    "ISTP": [
        ("🏔️ 홋카이도", "일본", "넓은 자연과 다양한 액티비티를 직접 경험하며 움직이기 좋아요.", "렌터카 여행이나 야외 활동처럼 직접 체험하는 코스를 추천해요."),
        ("🚗 제주", "대한민국", "자유롭게 이동하며 바다와 오름, 맛집을 취향대로 조합할 수 있어요.", "하루에 핵심 장소 2~3개만 정하고 나머지는 즉흥적으로!"),
        ("🌊 부산", "대한민국", "바다와 도시의 재미를 함께 즐기면서 활동적인 하루를 만들 수 있어요.", "해안 산책 후 새로운 먹거리를 하나 도전해보세요."),
    ],
    "ESFP": [
        ("🎉 오사카", "일본", "맛있는 음식과 쇼핑, 즐거운 거리가 가득해서 신나게 놀기 좋아요.", "도톤보리 먹방 + 쇼핑 코스로 기분 내기!"),
        ("🏖️ 발리", "인도네시아", "예쁜 풍경과 휴양, 다양한 체험을 한 번에 즐길 수 있어요.", "낮에는 체험, 저녁에는 여유로운 시간을 가져보세요."),
        ("🌴 괌", "괌", "바다에서 놀고 맛있는 것도 먹으며 가볍게 즐기기 좋은 휴양지예요.", "물놀이와 맛집을 번갈아 넣으면 지루하지 않아요."),
    ],
    "ESTP": [
        ("🏎️ 두바이", "아랍에미리트", "화려한 도시와 다양한 체험이 있어 액티브한 여행을 좋아한다면 잘 맞아요.", "하루에 새로운 체험 하나씩 넣어보세요."),
        ("🌊 부산", "대한민국", "바다, 액티비티, 먹거리까지 한 번에 즐길 수 있어 활동적인 여행에 좋아요.", "해양 액티비티와 야경 코스를 함께 넣어보세요."),
        ("🎢 홍콩", "홍콩", "짧은 시간에도 맛집·쇼핑·야경·도시 탐험을 알차게 즐길 수 있어요.", "낮부터 밤까지 동선을 촘촘하게 짜면 만족도가 높아요."),
    ],
    "ISFJ": [
        ("🌷 네덜란드", "네덜란드", "아기자기한 마을과 운하, 꽃 풍경을 차분하게 즐기기 좋아요.", "예쁜 마을 하나를 골라 천천히 둘러보세요."),
        ("🍵 교토", "일본", "차분한 분위기와 전통문화, 정돈된 공간에서 편안하게 여행할 수 있어요.", "아침 일찍 조용한 사찰을 방문해보세요."),
        ("🏡 전주", "대한민국", "한옥과 맛있는 음식, 여유로운 골목이 있어 부담 없이 여행하기 좋아요.", "한옥마을 산책 후 전통 디저트를 찾아보세요."),
    ],
    "ISTJ": [
        ("🏛️ 런던", "영국", "역사적인 명소와 박물관이 잘 정리되어 있어 계획적인 여행을 만들기 좋아요.", "관심 있는 박물관을 중심으로 동선을 먼저 짜보세요."),
        ("⛩️ 교토", "일본", "전통문화와 역사적 명소를 차근차근 둘러보며 알찬 여행을 할 수 있어요.", "지역별로 묶어서 이동하면 훨씬 편해요."),
        ("🏰 프라하", "체코", "역사적인 건축물과 구시가지를 걸으며 도시의 이야기를 느끼기 좋아요.", "구시가지→성 지구 순서로 걸어보는 코스를 추천해요."),
    ],
    "ESFJ": [
        ("💐 파리", "프랑스", "예쁜 장소와 맛있는 음식, 함께 추억을 만들 수 있는 공간이 많아요.", "카페와 사진 명소를 일정에 적당히 섞어보세요."),
        ("🍰 후쿠오카", "일본", "맛집과 쇼핑, 아기자기한 공간이 많아 함께 가기 좋은 여행지예요.", "친구들과 먹고 싶은 메뉴를 미리 하나씩 골라보세요."),
        ("🌊 부산", "대한민국", "바다와 카페, 맛집을 함께 즐기며 친구·가족과 추억을 만들기 좋아요.", "해운대나 광안리에서 야경까지 즐겨보세요."),
    ],
    "ENFJ": [
        ("🌉 시드니", "호주", "아름다운 풍경과 활기찬 도시가 어우러져 사람들과 좋은 추억을 만들기 좋아요.", "여럿이 함께 즐길 수 있는 체험 하나를 넣어보세요."),
        ("💖 파리", "프랑스", "문화와 예술, 맛있는 음식이 풍부해 감성적인 순간을 함께 나누기 좋아요.", "미술관 하나와 예쁜 카페 하나를 골라보세요."),
        ("🌺 하와이", "미국", "휴양과 액티비티를 함께 즐기며 소중한 사람들과 시간을 보내기 좋아요.", "하루는 바다, 하루는 관광처럼 분위기를 바꿔보세요."),
    ],
    "ENTJ": [
        ("🏙️ 뉴욕", "미국", "빠르게 움직이는 도시에서 다양한 경험을 효율적으로 쌓기 좋아요.", "보고 싶은 곳을 우선순위로 정해 동선을 최적화해보세요."),
        ("🇸🇬 싱가포르", "싱가포르", "깔끔한 도시 인프라와 다양한 볼거리를 짧은 일정에도 효율적으로 즐길 수 있어요.", "지역별로 묶어서 하루 코스를 만들어보세요."),
        ("🏗️ 두바이", "아랍에미리트", "현대적인 건축과 대형 프로젝트, 도시의 스케일을 직접 볼 수 있어요.", "건축·도시개발 명소를 중심으로 코스를 짜보세요."),
    ],
}

mbti_desc = {
    "INFP":"감성 가득한 몽상가 🌷", "INTP":"호기심 많은 아이디어 탐험가 🔍",
    "ENFP":"통통 튀는 모험가 🎈", "ENTP":"새로운 걸 좋아하는 발명가 💡",
    "ISFP":"취향이 확실한 감성 여행자 🎨", "ISTP":"직접 해보는 액션 탐험가 🧭",
    "ESFP":"즐거움을 찾아다니는 분위기 메이커 🎉", "ESTP":"스릴을 좋아하는 도전가 🚀",
    "ISFJ":"따뜻하고 세심한 힐링 여행자 🧸", "ISTJ":"꼼꼼한 계획형 탐험가 📋",
    "ESFJ":"함께라서 더 행복한 여행자 💕", "ESTJ":"효율적인 리더형 여행자 👑",
    "ENFJ":"사람과 추억을 사랑하는 여행자 💐", "ENTJ":"목표가 분명한 여행 설계자 🗺️",
}

# ---------- App ----------
st.markdown("""
<div class="hero">
  <div style="font-size:3.2rem;">🧳✨🌷</div>
  <div class="hero-title">MBTI 여행 콕콕</div>
  <div class="hero-sub">내 MBTI에 딱 맞는 여행지를 콕! 골라드릴게요 💗</div>
  <div style="margin-top:12px;">
    <span class="badge">🌸 귀염뽀짝</span>
    <span class="badge">🗺️ 여행 추천</span>
    <span class="badge">💌 MBTI 맞춤</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")
mbti = st.selectbox(
    "💗 나의 MBTI를 골라주세요",
    list(mbti_desc.keys()),
    format_func=lambda x: f"{x}  ·  {mbti_desc[x]}"
)

if st.button("🎀 여행지 추천받기", use_container_width=True):
    st.session_state["mbti"] = mbti
    st.session_state["show"] = True

if st.session_state.get("show"):
    selected = st.session_state["mbti"]
    st.markdown(f"### 💌 {selected}에게 도착한 여행 편지")
    st.markdown(
        f'<div style="text-align:center;color:#ff6f9d;font-weight:800;'
        f'font-size:1.15rem;">{mbti_desc[selected]}</div>',
        unsafe_allow_html=True
    )

    for i, (name, country, reason, tip) in enumerate(destinations[selected], 1):
        st.markdown(f"""
        <div class="place-card">
          <div class="place-name">{i}. {name}</div>
          <div style="color:#aa9cac;margin:4px 0 12px;">📍 {country}</div>
          <div class="reason"><b>왜 잘 맞을까요?</b><br>{reason}</div>
          <div class="tip">💡 콕콕 TIP · {tip}</div>
        </div>
        """, unsafe_allow_html=True)

    st.success("🌷 여행은 MBTI보다 '내가 좋아하는 것'이 제일 중요해요. 마음에 드는 곳을 골라 신나게 떠나봐요! 💕")

st.markdown('<div class="footer">made with 💗 for little travelers · MBTI는 재미로 참고해 주세요!</div>', unsafe_allow_html=True)
'''

path = Path("/mnt/data/mbti_travel_app.py")
path.write_text(app, encoding="utf-8")
print(f"완성했어요: {path}")
