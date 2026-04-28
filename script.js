let index = 0;
let answered = false;
let mode = "sequential";

let startIndex = 0;
let endIndex = 250;

let wrongAnswers = [];
let competitionQuestions = [];
let timer;
let timeLeft = 180;

// START QUIZ
function startQuiz(selectedMode) {
    mode = selectedMode;

    document.getElementById("startScreen").classList.add("hidden");
    document.getElementById("quizScreen").classList.remove("hidden");

    wrongAnswers = [];
    index = 0;
    startIndex = 0;

    timeLeft = 180;

    if (mode === "random") {
        questions = shuffle([...questions]);
    }

    if (mode === "competition") {
        competitionQuestions = shuffle([...questions]).slice(0, 3);
        startTimer();
        document.getElementById("navBar").classList.add("hidden");
    } else {
        document.getElementById("navBar").classList.remove("hidden");
        createNavigation();
    }

    loadQuestionFromRange();
}

// NAVIGACIJA
function createNavigation() {
    const nav = document.getElementById("navBar");
    nav.innerHTML = "";

    for (let i = 0; i < questions.length; i += 20) {
        const btn = document.createElement("button");
        btn.className = "navBtn";
        btn.innerText = `${i+1}-${Math.min(i+20, questions.length)}`;
        btn.onclick = () => {
            startIndex = i;
            index = 0;
            loadQuestionFromRange();
        };
        nav.appendChild(btn);
    }
}

function loadQuestionFromRange() {
    answered = false;

    const q = (mode === "competition")
        ? competitionQuestions[index]
        : questions[startIndex + index];

    if (!q) return;

    document.getElementById("question").innerText = q.q;

    ["A","B","C"].forEach(l => {
        const btn = document.getElementById(l);
        btn.innerText = l + ": " + q[l];
        btn.className = "";
        btn.disabled = false;
    });

    document.getElementById("nextBtn").classList.add("hidden");
}

function answer(letter) {
    if (answered) return;
    answered = true;

    const q = (mode === "competition")
        ? competitionQuestions[index]
        : questions[startIndex + index];

    if (letter !== q.correct) {
        wrongAnswers.push(q);
    }

    ["A","B","C"].forEach(l => {
        const btn = document.getElementById(l);
        btn.disabled = true;
        if (l === q.correct) btn.classList.add("correct");
        else if (l === letter) btn.classList.add("wrong");
    });

    document.getElementById("nextBtn").classList.remove("hidden");
}

function nextQuestion() {
    index++;

    const list = (mode === "competition")
        ? competitionQuestions
        : questions;

    if (index < list.length) loadQuestionFromRange();
    else endQuiz();
}

function endQuiz(manual = false) {
    clearInterval(timer);
    document.getElementById("quizScreen").innerHTML = `
        <h1>Konec kviza</h1>
        <p>Št. napačnih: ${wrongAnswers.length}</p>
        ${manual ? "<p>(Zaključeno ročno)</p>" : ""}
    `;
}

function startTimer() {
    document.getElementById("timer").classList.remove("hidden");

    timer = setInterval(() => {
        timeLeft--;
        document.getElementById("timer").innerText =
            `Čas: ${Math.floor(timeLeft/60)}:${String(timeLeft%60).padStart(2,"0")}`;
        if (timeLeft <= 0) {
            clearInterval(timer);
            endQuiz();
        }
    }, 1000);
}

function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
}