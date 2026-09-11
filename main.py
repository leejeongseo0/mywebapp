from pathlib import Path

code = r'''import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🍎 강아지 사과받기 게임",
    page_icon="🐶",
    layout="centered",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #eaf7ff 0%, #fffaf0 100%);
}
h1 {
    text-align: center;
    color: #5b5268;
}
.subtitle {
    text-align: center;
    color: #81778a;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🍎🐶 강아지 사과받기!</h1>", unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">마우스로 강아지를 움직여 떨어지는 사과를 받아보세요! 💕</div>',
    unsafe_allow_html=True
)

game_html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
* {
    box-sizing: border-box;
    user-select: none;
}

body {
    margin: 0;
    background: transparent;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

#game {
    position: relative;
    width: 100%;
    height: 620px;
    overflow: hidden;
    border-radius: 28px;
    border: 3px solid #ffffff;
    box-shadow: 0 10px 30px rgba(80,80,100,.15);
    background:
        radial-gradient(circle at 15% 15%, rgba(255,255,255,.9) 0 35px, transparent 36px),
        radial-gradient(circle at 80% 25%, rgba(255,255,255,.85) 0 28px, transparent 29px),
        linear-gradient(#9edcff 0%, #dff5ff 67%, #bde59c 67%, #91ce72 100%);
}

.cloud {
    position: absolute;
    font-size: 42px;
    opacity: .8;
    animation: cloudMove 18s linear infinite;
}

.cloud.one { top: 45px; left: -50px; }
.cloud.two { top: 145px; left: 55%; animation-duration: 24s; }

@keyframes cloudMove {
    from { transform: translateX(0); }
    to { transform: translateX(110vw); }
}

#score {
    position: absolute;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255,255,255,.92);
    padding: 9px 20px;
    border-radius: 999px;
    color: #66566e;
    font-weight: 800;
    font-size: 19px;
    z-index: 20;
}

#message {
    position: absolute;
    top: 60px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255,255,255,.9);
    padding: 8px 18px;
    border-radius: 999px;
    color: #e7658d;
    font-weight: 800;
    z-index: 20;
    opacity: 0;
    transition: opacity .2s;
}

#dog {
    position: absolute;
    bottom: 28px;
    left: 50%;
    width: 120px;
    height: 120px;
    transform: translateX(-50%);
    cursor: grab;
    z-index: 10;
    text-align: center;
}

#dogEmoji {
    font-size: 78px;
    line-height: 85px;
}

#basket {
    position: absolute;
    top: -5px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 43px;
    z-index: 11;
}

.apple {
    position: absolute;
    font-size: 38px;
    width: 45px;
    height: 45px;
    text-align: center;
    z-index: 5;
}

.pop {
    position: absolute;
    font-size: 48px;
    z-index: 30;
    pointer-events: none;
    animation: pop .7s ease-out forwards;
}

@keyframes pop {
    0% { transform: scale(.4) translateY(10px); opacity: 0; }
    35% { transform: scale(1.25); opacity: 1; }
    100% { transform: scale(1) translateY(-45px); opacity: 0; }
}

#startScreen {
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(3px);
    z-index: 50;
    display: flex;
    align-items: center;
    justify-content: center;
}

.startBox {
    text-align: center;
    background: white;
    border-radius: 28px;
    padding: 30px 35px;
    box-shadow: 0 12px 30px rgba(80,80,100,.16);
}

.startBox .big {
    font-size: 70px;
}

.startBox h2 {
    margin: 8px 0;
    color: #63556c;
}

.startBox p {
    color: #887b91;
}

#startButton {
    border: 0;
    border-radius: 999px;
    padding: 13px 30px;
    background: #ff91b4;
    color: white;
    font-size: 18px;
    font-weight: 800;
    cursor: pointer;
}

#startButton:hover {
    background: #ff709d;
}

#endScreen {
    display: none;
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,.78);
    backdrop-filter: blur(3px);
    z-index: 60;
    align-items: center;
    justify-content: center;
}

.endBox {
    text-align: center;
    background: white;
    border-radius: 28px;
    padding: 30px 40px;
    box-shadow: 0 12px 30px rgba(80,80,100,.16);
}

.endEmoji {
    font-size: 65px;
}

.endBox h2 {
    color: #63556c;
    margin: 5px;
}

#finalScore {
    color: #ff6f9d;
    font-size: 30px;
    font-weight: 800;
}

#restartButton {
    border: 0;
    border-radius: 999px;
    padding: 12px 28px;
    background: #8fcf75;
    color: white;
    font-size: 17px;
    font-weight: 800;
    cursor: pointer;
}
</style>
</head>

<body>

<div id="game">

    <div class="cloud one">☁️</div>
    <div class="cloud two">☁️</div>

    <div id="score">🍎 0개</div>
    <div id="message">😆 와아! 받았다!</div>

    <div id="dog">
        <div id="basket">🧺</div>
        <div id="dogEmoji">🐶</div>
    </div>

    <div id="startScreen">
        <div class="startBox">
            <div class="big">🐶🍎</div>
            <h2>사과를 받아주세요!</h2>
            <p>마우스로 강아지를 움직여<br>떨어지는 사과를 바구니에 받아요.</p>
            <button id="startButton">게임 시작하기 💕</button>
        </div>
    </div>

    <div id="endScreen">
        <div class="endBox">
            <div class="endEmoji">🐶✨</div>
            <h2>게임 끝!</h2>
            <p>강아지가 받은 사과는</p>
            <div id="finalScore">0개</div>
            <br>
            <button id="restartButton">다시 하기 🍎</button>
        </div>
    </div>

</div>

<script>
const game = document.getElementById("game");
const dog = document.getElementById("dog");
const scoreEl = document.getElementById("score");
const message = document.getElementById("message");
const startScreen = document.getElementById("startScreen");
const endScreen = document.getElementById("endScreen");
const startButton = document.getElementById("startButton");
const restartButton = document.getElementById("restartButton");
const finalScore = document.getElementById("finalScore");

let apples = [];
let score = 0;
let running = false;
let spawnTimer = null;
let gameTimer = null;
let timeLeft = 30;
let dogX = 50;
let mouseDown = false;

function moveDog(clientX) {
    const rect = game.getBoundingClientRect();
    let x = clientX - rect.left;

    const dogWidth = dog.offsetWidth;
    const minX = dogWidth / 2;
    const maxX = rect.width - dogWidth / 2;

    x = Math.max(minX, Math.min(maxX, x));

    dogX = x / rect.width * 100;
    dog.style.left = dogX + "%";
}

game.addEventListener("mousemove", (e) => {
    if (running) moveDog(e.clientX);
});

game.addEventListener("touchmove", (e) => {
    if (running && e.touches.length > 0) {
        moveDog(e.touches[0].clientX);
        e.preventDefault();
    }
}, {passive:false});

function showPopup(text, x, y) {
    const pop = document.createElement("div");
    pop.className = "pop";
    pop.textContent = text;
    pop.style.left = x + "px";
    pop.style.top = y + "px";
    game.appendChild(pop);

    setTimeout(() => pop.remove(), 700);
}

function updateScore() {
    scoreEl.textContent = "🍎 " + score + "개";
}

function showMessage(text) {
    message.textContent = text;
    message.style.opacity = "1";

    setTimeout(() => {
        message.style.opacity = "0";
    }, 600);
}

function createApple() {
    if (!running) return;

    const apple = document.createElement("div");
    apple.className = "apple";
    apple.textContent = "🍎";

    const maxX = game.clientWidth - 50;
    const x = Math.random() * maxX;

    apple.style.left = x + "px";
    apple.style.top = "-50px";

    game.appendChild(apple);

    apples.push({
        element: apple,
        x: x,
        y: -50,
        speed: 2.2 + Math.random() * 1.8
    });
}

function createBomb(x, y) {
    showPopup("💣", x, y);
}

function catchApple(apple, index) {
    const rect = dog.getBoundingClientRect();
    const gameRect = game.getBoundingClientRect();

    const dogLeft = rect.left - gameRect.left;
    const dogRight = dogLeft + rect.width;

    const appleCenter = apple.x + 22;

    if (
        apple.y + 35 >= game.clientHeight - 170 &&
        apple.y + 15 <= game.clientHeight - 40 &&
        appleCenter >= dogLeft &&
        appleCenter <= dogRight
    ) {
        score++;
        updateScore();

        const px = apple.x;
        const py = apple.y;

        showPopup("😆", px, py);
        showMessage("😆 와아! 받았다!");

        apple.element.remove();
        apples.splice(index, 1);

        return true;
    }

    return false;
}

function gameLoop() {
    if (!running) return;

    for (let i = apples.length - 1; i >= 0; i--) {

        const apple = apples[i];

        apple.y += apple.speed;
        apple.element.style.top = apple.y + "px";

        if (catchApple(apple, i)) {
            continue;
        }

        if (apple.y > game.clientHeight - 20) {

            createBomb(apple.x, game.clientHeight - 100);
            showMessage("💣 앗! 놓쳤어요!");

            apple.element.remove();
            apples.splice(i, 1);
        }
    }

    gameTimer = requestAnimationFrame(gameLoop);
}

function startGame() {

    apples.forEach(a => a.element.remove());
    apples = [];

    score = 0;
    timeLeft = 30;
    updateScore();

    running = true;

    startScreen.style.display = "none";
    endScreen.style.display = "none";

    createApple();

    spawnTimer = setInterval(() => {
        createApple();
    }, 900);

    gameLoop();

    setTimeout(() => {
        endGame();
    }, 30000);
}

function endGame() {

    if (!running) return;

    running = false;

    clearInterval(spawnTimer);
    cancelAnimationFrame(gameTimer);

    finalScore.textContent = score + "개";
    endScreen.style.display = "flex";
}

startButton.addEventListener("click", startGame);
restartButton.addEventListener("click", startGame);
</script>

</body>
</html>
"""

components.html(game_html, height=640, scrolling=False)

st.markdown("""
<div style="
text-align:center;
color:#9a8d9f;
font-size:13px;
padding:10px;
">
🍎 사과를 많이 받을수록 점수가 올라가요! · 💣 놓치면 폭탄이 뿅! · 🐶
</div>
""", unsafe_allow_html=True)
'''

path = Path("/mnt/data/app.py")
path.write_text(code, encoding="utf-8")
print(f"완성된 Streamlit 앱: {path}")
