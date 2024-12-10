from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL
                          )''')
        conn.commit()

init_db()

# Sample questions (your existing questions remain unchanged)
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

# Shuffle questions
import random
random.shuffle(QUESTIONS)

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('quiz'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()

            if user and check_password_hash(user[1], password):
                session['user_id'] = user[0]
                return redirect(url_for('quiz'))
            else:
                return "Invalid credentials, try again."

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return "Username already exists, try another."

    return render_template('signup.html')

@app.route('/quiz')
def quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/api/questions', methods=['GET'])
def get_questions():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"questions": QUESTIONS})

if __name__ == "__main__":
    app.run(debug=True)
