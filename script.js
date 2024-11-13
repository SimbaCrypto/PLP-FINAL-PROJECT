const questions = [
    {
        question: "What does SDG 4 focus on?",
        options: ["Zero Hunger", "Clean Water", "Climate Action",  "Quality Education"],
        answer: "Quality Education"
    },
    {
        question: "Which SDG aims to end poverty?",
        options: ["SDG 1", "SDG 5", "SDG 10", "SDG 17"],
        answer: "SDG 1"
    },
    {
        question: "What is the goal of SDG 3?",
        options: ["Affordable and Clean Energy", "Gender Equality",  "Good Health and Well-being", "Responsible Consumption"],
        answer: "Good Health and Well-being"
    }

    
    // Add more questions here...
];

let score = 0;
let currentQuestionIndex = 0;

function displayQuestion() {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = "";

    const question = questions[currentQuestionIndex];
    const questionElement = document.createElement("div");
    questionElement.classList.add("question");
    questionElement.innerHTML = `<h2>${question.question}</h2>`;
    
    question.options.forEach(option => {
        const button = document.createElement("button");
        button.innerText = option;
        button.onclick = () => checkAnswer(option);
        questionElement.appendChild(button);
    });

    quizContainer.appendChild(questionElement);
}

function checkAnswer(selectedOption) {
    const question = questions[currentQuestionIndex];
    if (selectedOption === question.answer) {
        score++;
        alert("Correct!");
    } else {
        alert("Incorrect! The correct answer was: " + question.answer);
    }
    currentQuestionIndex++;

    if (currentQuestionIndex < questions.length) {
        displayQuestion();
    } else {
        showScore();
    }
}

function showScore() {
    document.getElementById("quiz-container").style.display = "none";
    document.getElementById("score-container").style.display = "block";
    document.getElementById("score").innerText = score + " out of " + questions.length;
}

function restartQuiz() {
    score = 0;
    currentQuestionIndex = 0;
    document.getElementById("score-container").style.display = "none";
    displayQuestion();
}

// Start the quiz
displayQuestion();
