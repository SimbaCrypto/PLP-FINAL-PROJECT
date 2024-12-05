from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

# Sample questions
QUESTIONS = [
    {
        "id": 1,
        "question": "Which SDG aims to end poverty in all its forms everywhere?",
        "answers": ["SDG 3", "SDG 2", "SDG 1", "SDG 4"],
        "correct": 2
    },
    {
        "id": 2,
        "question": "What is the primary focus of SDG 13?",
        "answers": ["Affordable and Clean Energy", "Quality Education", "Climate Action", "Clean Water and Sanitation"],
        "correct": 2
    },
    {
        "id": 3,
        "question": "What does SDG 7 focus on?",
        "answers": ["Life on Land", "Decent Work and Economic Growth", "Affordable and Clean Energy", "Sustainable Cities and Communities"],
        "correct": 2
    },
    {
        "id": 4,
        "question": "Which SDG focuses on ensuring healthy lives and promoting well-being?",
        "answers": ["SDG 6", "SDG 3", "SDG 8", "SDG 12"],
        "correct": 1
    },
    {
        "id": 5,
        "question": "What is the target year for achieving the SDGs?",
        "answers": ["2030", "2040", "2025", "2050"],
        "correct": 0
    },
    {
        "id": 6,
        "question": "Which SDG emphasizes partnerships for the goals?",
        "answers": ["SDG 17", "SDG 16", "SDG 15", "SDG 14"],
        "correct": 0
    },
    {
        "id": 7,
        "question": "What does SDG stand for?",
        "answers": ["Social Development Growth", "Strategic Development Goal", "Sustainable Development Goal", "Standard Development Guide"],
        "correct": 2
    },
    {
        "id": 8,
        "question": "How many Sustainable Development Goals (SDGs) are there?",
        "answers": ["12", "17", "20", "15"],
        "correct": 1
    },
    {
        "id": 9,
        "question": "Which SDG is dedicated to achieving gender equality?",
        "answers": ["SDG 3", "SDG 5", "SDG 7", "SDG 10"],
        "correct": 1
    },
    {
        "id": 10,
        "question": "SDG 14 focuses on which of the following?",
        "answers": ["Responsible Consumption and Production", "Industry, Innovation, and Infrastructure", "Life Below Water", "Life on Land"],
        "correct": 2
    }
    
]


# Shuffle the questions
random.shuffle(QUESTIONS)

# Shuffle the answers for each question
for question in QUESTIONS:
    random.shuffle(question["answers"])
    # Update the correct index to match the shuffled answers
    question["correct"] = question["answers"].index(question["answers"][question["correct"]])


# Route to serve the HTML frontend
@app.route('/')
def index():
    return render_template('index.html')

# API to fetch questions
@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify({"questions": QUESTIONS})

if __name__ == "__main__":
    app.run(debug=True)
