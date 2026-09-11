import streamlit as st

# =========================================================
# 기본 설정
# =========================================================

st.set_page_config(
    page_title="MBTI 여행 콕콕 💗",
    page_icon="🌷",
    layout="centered"
)


# =========================================================
# CSS - 귀엽고 깜찍한 디자인
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffe8f1 0%, transparent 28%),
        radial-gradient(circle at 90% 15%, #e8f4ff 0%, transparent 28%),
        linear-gradient(180deg, #fffafd 0%, #f7fbff 100%);
}

/* 제목 */
h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
    color: #5f5068;
}

/* 메인 배너 */
.hero {
    text-align: center;
    padding: 30px 20px 25px;
    background: rgba(255, 255, 255, 0.82);
    border: 2px solid #ffd9e8;
    border-radius: 30px;
    box-shadow: 0 12px 35px rgba(110, 80, 110, 0.10);
    margin-bottom: 25px;
}

.hero-icon {
    font-size: 55px;
}

.hero-title {
    font-family: 'Jua', sans-serif;
    font-size: 45px;
    color: #ff6f9d;
    margin-top: 5px;
}

.hero-subtitle {
    color: #817184;
    font-size: 17px;
    margin-top: 8px;
}

/* 배지 */
.badge {
    display: inline-block;
    padding: 7px 14px;
    margin: 10px 3px 0;
    border-radius: 30px;
    background: #fff0f6;
    color: #e85f8e;
    font-weight: 800;
}

/* 선택창 */
div[data-testid="stSelectbox"] label {
    color: #66566d;
    font-weight: 800;
    font-size: 16px;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    border-radius: 20px;
    border: 2px solid #ffd0e1;
    background: linear-gradient(135deg, #ffffff, #fff0f6);
    color: #d95687;
    font-weight: 800;
    font-size: 17px;
    padding: 12px;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #ff9fc2;
    color: #ff4f89;
    transform: translateY(-2px);
}

/* MBTI 설명 */
.mbti-box {
    text-align: center;
    background: #fff4f8;
    border-radius: 20px;
    padding: 15px;
    margin: 15px 0 20px;
    color: #756678;
}

/* 여행지 카드 */
.place-card {
    background: white;
    border: 2px solid #f1e4ed;
    border-radius: 25px;
    padding: 22px;
    margin: 15px 0;
    box-shadow: 0 8px 22px rgba(100, 80, 110, 0.08);
}

.place-number {
    color: #ff8db2;
    font-weight: 800;
    font-size: 14px;
}

.place-name {
    font-family: 'Jua', sans-serif;
    font-size: 29px;
    color: #62526b;
    margin-top: 3px;
}

.country {
    color: #a294a8;
    margin-bottom: 13px;
}

.reason-title {
    color: #e45f8d;
    font-weight: 800;
}

.reason {
    color: #756878;
    line-height: 1.7;
}

.tip {
    background: #fff8dc;
    border-radius: 16px;
    padding: 13px 15px;
    margin-top: 14px;
    color: #76652f;
    line-height: 1.5;
}

/* 하단 */
.footer {
    text-align: center;
    color: #a093a5;
    font-size: 13px;
    padding: 25px 0 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# MBTI별 여행지 데이터
# =========================================================

travel_data = {

    "INFP": {
        "description": "감성 가득한 몽상가 🌷",
        "places": [
            {
                "name": "🌿 교토",
                "country": "🇯🇵 일본",
                "reason": "조용한 골목과 사찰, 아름다운 계절 풍경 속에서 천천히 나만의 시간을 보내기 좋아요.",
                "tip": "아라시야마를 산책하고 작은 카페에서 여유롭게 쉬어보세요."
            },
            {
                "name": "🌊 제주",
                "country": "🇰🇷 대한민국",
                "reason": "바다와 오름 같은 자연을 바라보며 생각을 정리하고 감성을 충전하기 좋은 곳이에요.",
                "tip": "바다 산책 후 노을 명소에서 잠시 멍때려보세요."
            },
            {
                "name": "🎨 파리",
                "country": "🇫🇷 프랑스",
                "reason": "예쁜 거리와 미술관, 작은 서점과 카페가 감성을 자극하는 도시예요.",
                "tip": "유명 관광지만 따라가기보다 골목을 천천히 걸어보세요."
            }
        ]
    },

    "INFJ": {
        "description": "조용하지만 깊이 있는 여행자 🌙",
        "places": [
            {
                "name": "🌿 교토",
                "country": "🇯🇵 일본",
                "reason": "전통적인 공간과 고요한 분위기 속에서 생각을 정리하고 마음을 쉬게 하기 좋아요.",
                "tip": "사람이 적은 아침 시간에 사찰이나 정원을 방문해보세요."
            },
            {
                "name": "📚 런던",
                "country": "🇬🇧 영국",
                "reason": "역사와 문화를 깊이 있게 살펴볼 수 있는 박물관과 공간이 많아요.",
                "tip": "관심 있는 주제의 박물관 하나를 정해서 천천히 둘러보세요."
            },
            {
                "name": "🌊 제주",
                "country": "🇰🇷 대한민국",
                "reason": "자연 속에서 혼자만의 시간을 보내며 생각을 정리하기 좋은 여행지예요.",
                "tip": "해안 산책로를 따라 걸으며 음악을 들어보세요."
            }
        ]
    },

    "INTP": {
        "description": "호기심 많은 아이디어 탐험가 🔍",
        "places": [
            {
                "name": "🔭 도쿄",
                "country": "🇯🇵 일본",
                "reason": "최신 기술부터 독특한 문화와 서브컬처까지 새로운 것을 탐구할 거리가 정말 많아요.",
                "tip": "과학관, 전자상가, 서브컬처 공간 중 관심 있는 곳을 골라 깊게 탐험해보세요."
            },
            {
                "name": "🏛️ 런던",
                "country": "🇬🇧 영국",
                "reason": "과학·역사·자연사 등 다양한 분야의 콘텐츠를 직접 살펴볼 수 있어요.",
                "tip": "무료 박물관 하나를 골라 관심 분야부터 집중적으로 살펴보세요."
            },
            {
                "name": "🧪 싱가포르",
                "country": "🇸🇬 싱가포르",
                "reason": "미래적인 도시 풍경과 과학, 자연이 조화를 이루어 새로운 것을 발견하는 재미가 있어요.",
                "tip": "가든스 바이 더 베이와 과학 관련 공간을 함께 둘러보세요."
            }
        ]
    },

    "INTJ": {
        "description": "계획을 세우고 세상을 분석하는 전략가 🧠",
        "places": [
            {
                "name": "🏙️ 싱가포르",
                "country": "🇸🇬 싱가포르",
                "reason": "깔끔한 도시 시스템과 현대적인 건축물을 효율적으로 둘러보기 좋아요.",
                "tip": "지역별로 여행지를 묶어 효율적인 동선을 만들어보세요."
            },
            {
                "name": "🏛️ 런던",
                "country": "🇬🇧 영국",
                "reason": "역사와 과학, 예술 등 관심 분야를 체계적으로 탐험하기 좋은 도시예요.",
                "tip": "미리 관심 장소를 지도에 저장해서 동선을 최적화해보세요."
            },
            {
                "name": "🏗️ 두바이",
                "country": "🇦🇪 아랍에미리트",
                "reason": "현대적인 건축물과 거대한 도시 프로젝트를 직접 볼 수 있어요.",
                "tip": "건축과 도시개발에 관심이 있다면 관련 명소를 중심으로 계획해보세요."
            }
        ]
    },

    "ENFP": {
        "description": "통통 튀는 모험가 🎈",
        "places": [
            {
                "name": "🎡 런던",
                "country": "🇬🇧 영국",
                "reason": "다양한 사람과 문화, 예상하지 못한 재미있는 장소를 만날 수 있어요.",
                "tip": "하루에 한 곳 정도는 계획 없이 즉흥적으로 찾아가보세요."
            },
            {
                "name": "🌺 방콕",
                "country": "🇹🇭 태국",
                "reason": "맛있는 음식과 활기찬 거리, 색다른 문화가 가득해서 에너지가 팡팡 올라가요.",
                "tip": "시장과 야경 스팟을 함께 넣어보세요."
            },
            {
                "name": "🌈 오사카",
                "country": "🇯🇵 일본",
                "reason": "먹거리와 쇼핑, 재미있는 명소가 많아서 신나게 돌아다니기 좋아요.",
                "tip": "맛집 하나만 정하고 나머지는 현장에서 골라보세요."
            }
        ]
    },

    "ENFJ": {
        "description": "사람과 추억을 사랑하는 여행자 💐",
        "places": [
            {
                "name": "🌉 시드니",
                "country": "🇦🇺 호주",
                "reason": "아름다운 풍경과 활기찬 도시가 어우러져 함께 좋은 추억을 만들기 좋아요.",
                "tip": "여럿이 함께 즐길 수 있는 체험을 하나 넣어보세요."
            },
            {
                "name": "💖 파리",
                "country": "🇫🇷 프랑스",
                "reason": "예술과 문화, 맛있는 음식이 풍부해서 소중한 사람과 추억을 만들기 좋아요.",
                "tip": "미술관과 예쁜 카페를 일정에 함께 넣어보세요."
            },
            {
                "name": "🌺 하와이",
                "country": "🇺🇸 미국",
                "reason": "휴양과 액티비티를 함께 즐기며 가족이나 친구들과 시간을 보내기 좋아요.",
                "tip": "하루는 바다, 하루는 관광처럼 분위기를 바꿔보세요."
            }
        ]
    },

    "ENTP": {
        "description": "새로운 것을 좋아하는 아이디어 뱅크 💡",
        "places": [
            {
                "name": "🏙️ 뉴욕",
                "country": "🇺🇸 미국",
                "reason": "끊임없이 새로운 사람과 문화, 아이디어를 만날 수 있어 지루할 틈이 없어요.",
                "tip": "동네 하나를 정해서 예상 밖의 가게나 전시를 찾아보세요."
            },
            {
                "name": "🚀 베를린",
                "country": "🇩🇪 독일",
                "reason": "개성 있는 문화와 실험적인 공간이 많아서 호기심을 자극해요.",
                "tip": "유명 관광지보다 독립적인 문화 공간을 찾아보세요."
            },
            {
                "name": "🎮 도쿄",
                "country": "🇯🇵 일본",
                "reason": "전통부터 최신 기술과 대중문화까지 서로 다른 세계를 한 도시에서 만날 수 있어요.",
                "tip": "하루에 서로 다른 분위기의 지역을 여러 곳 탐험해보세요."
            }
        ]
    },

    "ENTJ": {
        "description": "목표가 분명한 여행 설계자 🗺️",
        "places": [
            {
                "name": "🏙️ 뉴욕",
                "country": "🇺🇸 미국",
                "reason": "빠르게 움직이는 도시에서 다양한 경험을 효율적으로 쌓을 수 있어요.",
                "tip": "보고 싶은 장소를 우선순위로 정하고 동선을 최적화해보세요."
            },
            {
                "name": "🇸🇬 싱가포르",
                "country": "🇸🇬 싱가포르",
                "reason": "깔끔한 도시 인프라와 다양한 볼거리를 짧은 일정에도 효율적으로 즐길 수 있어요.",
                "tip": "지역별로 묶어서 하루 코스를 만들어보세요."
            },
            {
                "name": "🏗️ 두바이",
                "country": "🇦🇪 아랍에미리트",
                "reason": "현대적인 건축과 대형 프로젝트, 도시의 엄청난 스케일을 직접 볼 수 있어요.",
                "tip": "건축·도시개발 명소를 중심으로 코스를 짜보세요."
            }
        ]
    },

    "ISFP": {
        "description": "취향이 확실한 감성 여행자 🎨",
        "places": [
            {
                "name": "🌸 후쿠오카",
                "country": "🇯🇵 일본",
                "reason": "맛있는 음식과 아늑한 골목, 바다까지 부담 없이 즐길 수 있어요.",
                "tip": "카페 한 곳과 바닷가 산책처럼 느슨한 일정을 만들어보세요."
            },
            {
                "name": "🏝️ 다낭",
                "country": "🇻🇳 베트남",
                "reason": "아름다운 자연과 편안한 분위기 속에서 쉬면서 소소한 즐거움을 찾기 좋아요.",
                "tip": "일정을 빡빡하게 채우기보다 휴식 시간을 남겨두세요."
            },
            {
                "name": "🌿 제주",
                "country": "🇰🇷 대한민국",
                "reason": "자연과 맛집, 감성적인 공간을 내 취향대로 골라 즐길 수 있어요.",
                "tip": "사진 찍기 좋은 자연 명소 하나를 골라 천천히 즐겨보세요."
            }
        ]
    },

    "ISTP": {
        "description": "직접 해보는 액션 탐험가 🧭",
        "places": [
            {
                "name": "🏔️ 홋카이도",
                "country": "🇯🇵 일본",
                "reason": "넓은 자연과 다양한 액티비티를 직접 경험하며 움직이기 좋아요.",
                "tip": "자연 속 체험이나 야외 활동을 하나 넣어보세요."
            },
            {
                "name": "🚗 제주",
                "country": "🇰🇷 대한민국",
                "reason": "바다와 오름, 맛집을 자유롭게 조합하면서 원하는 대로 움직일 수 있어요.",
                "tip": "핵심 장소 2~3개만 정하고 나머지는 즉흥적으로 결정해보세요."
            },
            {
                "name": "🌊 부산",
                "country": "🇰🇷 대한민국",
                "reason": "바다와 도시의 재미를 함께 즐기면서 활동적인 하루를 만들 수 있어요.",
                "tip": "해안 산책과 새로운 먹거리 도전을 함께 해보세요."
            }
        ]
    },

    "ISTJ": {
        "description": "꼼꼼한 계획형 탐험가 📋",
        "places": [
            {
                "name": "🏛️ 런던",
                "country": "🇬🇧 영국",
                "reason": "역사적인 명소와 박물관이 잘 정리되어 있어 계획적인 여행을 만들기 좋아요.",
                "tip": "관심 있는 박물관을 중심으로 동선을 먼저 짜보세요."
            },
            {
                "name": "⛩️ 교토",
                "country": "🇯🇵 일본",
                "reason": "전통문화와 역사적 명소를 차근차근 둘러보며 알찬 여행을 할 수 있어요.",
                "tip": "지역별로 관광지를 묶어서 이동하면 편리해요."
            },
            {
                "name": "🏰 프라하",
                "country": "🇨🇿 체코",
                "reason": "역사적인 건축물과 구시가지를 걸으며 도시의 이야기를 느끼기 좋아요.",
                "tip": "구시가지와 성 지구를 나누어 계획해보세요."
            }
        ]
    },

    "ISFJ": {
        "description": "따뜻하고 세심한 힐링 여행자 🧸",
        "places": [
            {
                "name": "🌷 네덜란드",
                "country": "🇳🇱 네덜란드",
                "reason": "아기자기한 마을과 운하, 꽃 풍경을 차분하게 즐기기 좋아요.",
                "tip": "예쁜 마을 하나를 골라 천천히 둘러보세요."
            },
            {
                "name": "🍵 교토",
                "country": "🇯🇵 일본",
                "reason": "차분한 분위기와 전통문화, 정돈된 공간에서 편안하게 여행할 수 있어요.",
                "tip": "아침 일찍 조용한 사찰을 방문해보세요."
            },
            {
                "name": "🏡 전주",
                "country": "🇰🇷 대한민국",
                "reason": "한옥과 맛있는 음식, 여유로운 골목이 있어 부담 없이 여행하기 좋아요.",
                "tip": "한옥마을 산책 후 전통 디저트를 찾아보세요."
            }
        ]
    },

    "ESFP": {
        "description": "즐거움을 찾아다니는 분위기 메이커 🎉",
        "places": [
            {
                "name": "🎉 오사카",
                "country": "🇯🇵 일본",
                "reason": "맛있는 음식과 쇼핑, 즐거운 거리가 가득해서 신나게 놀기 좋아요.",
                "tip": "먹방과 쇼핑을 함께 넣어 기분 좋은 하루를 만들어보세요."
            },
            {
                "name": "🏖️ 발리",
                "country": "🇮🇩 인도네시아",
                "reason": "예쁜 풍경과 휴양, 다양한 체험을 한 번에 즐길 수 있어요.",
                "tip": "낮에는 체험, 저녁에는 여유로운 시간을 가져보세요."
            },
            {
                "name": "🌴 괌",
                "country": "🇬🇺 괌",
                "reason": "바다에서 놀고 맛있는 것도 먹으며 가볍게 즐기기 좋은 휴양지예요.",
                "tip": "물놀이와 맛집을 번갈아 넣어보세요."
            }
        ]
    },

    "ESTP": {
        "description": "스릴을 좋아하는 도전가 🚀",
        "places": [
            {
                "name": "🏎️ 두바이",
                "country": "🇦🇪 아랍에미리트",
                "reason": "화려한 도시와 다양한 체험이 있어 액티브한 여행을 좋아한다면 잘 맞아요.",
                "tip": "새로운 체험을 하나씩 넣어 여행의 재미를 높여보세요."
            },
            {
                "name": "🌊 부산",
                "country": "🇰🇷 대한민국",
                "reason": "바다, 액티비티, 먹거리까지 한 번에 즐길 수 있어 활동적인 여행에 좋아요.",
                "tip": "해양 액티비티와 야경 코스를 함께 넣어보세요."
            },
            {
                "name": "🎢 홍콩",
                "country": "🇭🇰 홍콩",
                "reason": "짧은 시간에도 맛집·쇼핑·야경·도시 탐험을 알차게 즐길 수 있어요.",
                "tip": "낮부터 밤까지 다양한 활동을 골고루 넣어보세요."
            }
        ]
    },

    "ESFJ": {
        "description": "함께라서 더 행복한 여행자 💕",
        "places": [
            {
                "name": "💐 파리",
                "country": "🇫🇷 프랑스",
                "reason": "예쁜 장소와 맛있는 음식, 함께 추억을 만들 수 있는 공간이 많아요.",
                "tip": "카페와 사진 명소를 일정에 적당히 섞어보세요."
            },
            {
                "name": "🍰 후쿠오카",
                "country": "🇯🇵 일본",
                "reason": "맛집과 쇼핑, 아기자기한 공간이 많아 친구나 가족과 가기 좋아요.",
                "tip": "함께 먹고 싶은 메뉴를 하나씩 골라보세요."
            },
            {
                "name": "🌊 부산",
                "country": "🇰🇷 대한민국",
                "reason": "바다와 카페, 맛집을 함께 즐기며 좋은 추억을 만들기 좋아요.",
                "tip": "광안리에서 맛있는 것을 먹고 야경까지 즐겨보세요."
            }
        ]
    }
}


# =========================================================
# 메인 화면
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-icon">
        🧳✨🌷
    </div>

    <div class="hero-title">
        MBTI 여행 콕콕
    </div>

    <div class="hero-subtitle">
        내 MBTI에 딱 맞는 여행지를 콕! 골라드릴게요 💗
    </div>

    <div>
        <span class="badge">🌸 귀염뽀짝</span>
        <span class="badge">🗺️ 여행 추천</span>
        <span class="badge">💌 MBTI 맞춤</span>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# MBTI 선택
# =========================================================

st.markdown("### 💗 나의 MBTI를 골라주세요!")

mbti_list = list(travel_data.keys())

selected_mbti = st.selectbox(
    "MBTI 선택",
    mbti_list,
    format_func=lambda x: f"{x}  ·  {travel_data[x]['description']}",
    label_visibility="collapsed"
)


# =========================================================
# 추천 버튼
# =========================================================

st.write("")

recommend = st.button(
    "🎀 여행지 추천받기 ✈️",
    use_container_width=True
)


# =========================================================
# 추천 결과
# =========================================================

if recommend:

    data = travel_data[selected_mbti]

    st.markdown(
        f"""
        <div class="mbti-box">
            <div style="font-size:32px;">💌</div>
            <b style="font-size:22px; color:#ff6f9d;">
                {selected_mbti}
            </b>
            <br>
            <span style="font-size:16px;">
                {data['description']}
            </span>
            <br><br>
            오늘은 어떤 여행지가 마음에 쏙 들까요? 🌷
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "### 🌷 당신에게 추천하는 여행지"
    )

    for index, place in enumerate(data["places"], start=1):

        st.markdown(
            f"""
            <div class="place-card">

                <div class="place-number">
                    RECOMMEND {index}
                </div>

                <div class="place-name">
                    {place['name']}
                </div>

                <div class="country">
                    {place['country']}
                </div>

                <div class="reason-title">
                    💗 왜 잘 맞을까요?
                </div>

                <div class="reason">
                    {place['reason']}
                </div>

                <div class="tip">
                    💡 <b>콕콕 TIP</b><br>
                    {place['tip']}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.success(
        "🌸 마음에 드는 곳을 발견했다면 여행 계획을 세워볼까요? "
        "MBTI는 재미로 참고하고, 결국 내가 좋아하는 여행이 가장 좋은 여행이에요! 💕"
    )


# =========================================================
# 푸터
# =========================================================

st.markdown(
    """
    <div class="footer">
        🧳 MBTI 여행 콕콕 · made with 💗<br>
        MBTI는 여행 성향을 재미있게 알아보기 위한 참고용이에요 🌷
    </div>
    """,
    unsafe_allow_html=True
)
