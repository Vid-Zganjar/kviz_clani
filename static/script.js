let questions = [];
let index = 0;
let answered = false;
let mode = "sequential";

let startIndex = 0;
let endIndex = 250;

let wrongAnswers = [];
let competitionQuestions = [];
let timer;
let timeLeft = 180;

// LOAD QUESTIONS
fetch("/questions")
    .then(r => r.json())
    .then(data => {
        questions = data;
    });


// START QUIZ
function startQuiz(selectedMode) {
    mode = selectedMode;

    document.getElementById("startScreen").classList.add("hidden");
    document.getElementById("quizScreen").classList.remove("hidden");

    wrongAnswers = [];
    index = 0;
    startIndex = 0;
    endIndex = 250;

      // 👉 RESET TIMER
    timeLeft = 180;

    if (mode === "random") {
        questions = shuffle([...questions]);
    }

    if (mode === "competition") {
        competitionQuestions = shuffle([...questions]).slice(0, 3);
        startTimer();

        // 🔥 SKRIJ NAVIGACIJO
        document.getElementById("navBar").classList.add("hidden");
    } else {
        // 👉 prikaži navigacijo samo v učenju
        document.getElementById("navBar").classList.remove("hidden");
        createNavigation();
    }

    loadQuestionFromRange();
}


// NAVIGACIJA (1–20, 21–40 ...)
function createNavigation() {
    const nav = document.getElementById("navBar");
    nav.innerHTML = "";

    for (let i = 0; i < 250; i += 20) {
        const btn = document.createElement("button");
        btn.className = "navBtn";

        let from = i + 1;
        let to = Math.min(i + 20, 250);

        btn.innerText = `${from}-${to}`;

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


// ANSWER
function answer(letter) {
    if (answered) return;
    answered = true;

    const q = (mode === "competition")
        ? competitionQuestions[index]
        : questions[startIndex + index];

    const correct = q.correct;

    if (letter !== correct) {
        wrongAnswers.push(q);
    }

    ["A","B","C"].forEach(l => {
        const btn = document.getElementById(l);
        btn.disabled = true;

        if (l === correct) btn.classList.add("correct");
        else if (l === letter) btn.classList.add("wrong");
    });

    document.getElementById("nextBtn").classList.remove("hidden");
}


// NEXT QUESTION
function nextQuestion() {
    index++;

    const list = (mode === "competition")
        ? competitionQuestions
        : questions;

    if (mode === "competition") {
        if (index < list.length) {
            loadQuestionFromRange();
        } else {
            endQuiz();
        }
        return;
    }

    if (startIndex + index < endIndex && startIndex + index < questions.length) {
        loadQuestionFromRange();
    } else {
        endQuiz();
    }
}


// END (lahko kadarkoli)
function endQuiz(manual = false) {
    clearInterval(timer);
document.getElementById("navBar").classList.add("hidden");
    document.getElementById("quizScreen").innerHTML = `
        <h1>Konec kviza</h1>
        <p>Št. napačnih: ${wrongAnswers.length}</p>
        ${manual ? "<p>(Kviz zaključen ročno)</p>" : ""}
    `;

    if (wrongAnswers.length > 0) {
        document.getElementById("quizScreen").innerHTML += `
            <h3>Napačna vprašanja:</h3>
            <ul>
                ${wrongAnswers.map(q => `<li>${q.q}</li>`).join("")}
            </ul>
        `;
    }
}


// TIMER (competition)
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


// SHUFFLE
function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
}