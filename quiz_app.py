import random

questions = [
    {
        "question": "What does SDG 4 focus on?",
        "options": ["1) Quality Education", "2) Clean Water", "3) Climate Action", "4) Zero Hunger"],
        "answer": "1"
    },
    {
        "question": "Which SDG aims to end poverty?",
        "options": ["1) SDG 1", "2) SDG 5", "3) SDG 10", "4) SDG 17"],
        "answer": "1"
    },

    {
    "question": "What is the focus of SDG 3?",
    "options": ["1) Good Health and Well-being", "2) Gender Equality", "3) Affordable and Clean Energy", "4) Responsible Consumption"],
    "answer": "1"
},
{
    "question": "Which SDG aims to achieve gender equality?",
    "options": ["1) SDG 6", "2) SDG 3", "3) SDG 5", "4) SDG 8"],
    "answer": "3"
},
{
    "question": "What does SDG 13 aim to address?",
    "options": ["1) Life Below Water", "2) Climate Action", "3) Reduced Inequalities", "4) Sustainable Cities"],
    "answer": "2"
},
{
    "question": "Which SDG is focused on ensuring clean water and sanitation for all?",
    "options": ["1) SDG 7", "2) SDG 6", "3) SDG 2", "4) SDG 10"],
    "answer": "2"
},
{
    "question": "Which SDG aims to promote decent work and economic growth?",
    "options": ["1) SDG 11", "2) SDG 8", "3) SDG 15", "4) SDG 4"],
    "answer": "2"
},
{
    "question": "What is the goal of SDG 15?",
    "options": ["1) Life on Land", "2) No Poverty", "3) Quality Education", "4) Affordable and Clean Energy"],
    "answer": "1"
},

{
    "question": "Which SDG focuses on reducing inequalities within and among countries?",
    "options": ["1) SDG 9", "2) SDG 13", "3) SDG 10", "4) SDG 7"],
    "answer": "3"
},

{
    "question": "Which SDG is focused on promoting peace, justice, and strong institutions?",
    "options": ["1) SDG 16", "2) SDG 9", "3) SDG 3", "4) SDG 12"],
    "answer": "1"
},
{
    "question": "What is the goal of SDG 2?",
    "options": ["1) Zero Hunger", "2) No Poverty", "3) Clean Water and Sanitation", "4) Climate Action"],
    "answer": "1"
},
{
    "question": "SDG 7 focuses on which of the following?",
    "options": ["1) Industry, Innovation, and Infrastructure", "2) Affordable and Clean Energy", "3) Life Below Water", "4) Good Health and Well-being"],
    "answer": "2"
},
{
    "question": "Which SDG aims to ensure sustainable consumption and production patterns?",
    "options": ["1) SDG 12", "2) SDG 2", "3) SDG 8", "4) SDG 6"],
    "answer": "1"
},
{
    "question": "SDG 9 focuses on which of the following areas?",
    "options": ["1) Clean Water and Sanitation", "2) Quality Education", "3) Industry, Innovation, and Infrastructure", "4) Life on Land"],
    "answer": "3"
},
{
    "question": "What does SDG 11 aim to create?",
    "options": ["1) Partnerships for the Goals", "2) Peace, Justice, and Strong Institutions", "3) Sustainable Cities and Communities", "4) Climate Action"],
    "answer": "3"
},
{
    "question": "Which SDG is about conserving and sustainably using the oceans, seas, and marine resources?",
    "options": ["1) SDG 14", "2) SDG 6", "3) SDG 15", "4) SDG 13"],
    "answer": "1"
},
{
    "question": "SDG 17 is aimed at strengthening which of the following?",
    "options": ["1) Quality Education", "2) Global Partnerships for Sustainable Development", "3) Industry and Innovation", "4) Climate Action"],
    "answer": "2"
},
{
    "question": "Which SDG focuses on ending poverty in all its forms everywhere?",
    "options": ["1) SDG 10", "2) SDG 5", "3) SDG 1", "4) SDG 8"],
    "answer": "3"
},
{
    "question": "What does SDG 5 aim to achieve?",
    "options": ["1) Gender Equality", "2) Decent Work and Economic Growth", "3) Clean Water and Sanitation", "4) Quality Education"],
    "answer": "1"
}
]

def display_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)

def get_answer():
    return input("Your answer (choose the number of the option): ")

def check_answer(question, user_answer):
    return user_answer == question["answer"]

def run_quiz():
    score = 0
    random.shuffle(questions)  # Questions set to reshuffle for variety
    for question in questions:
        display_question(question)
        user_answer = get_answer()
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer was:", question["answer"])

    print(f"\nYou scored {score} out of {len(questions)}")

if __name__ == "__main__":
    print("Welcome to the SDG Educational Quiz!")
    run_quiz()
