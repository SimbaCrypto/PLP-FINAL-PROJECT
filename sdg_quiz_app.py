import tkinter as tk
import random

# List of questions
questions = [
    {
        "question": "What does SDG 4 focus on?",
        "options": ["Quality Education", "Clean Water", "Climate Action", "Zero Hunger"],
        "answer": "Quality Education"
    },
    {
        "question": "Which SDG aims to end poverty?",
        "options": ["SDG 1", "SDG 5", "SDG 10", "SDG 17"],
        "answer": "SDG 1"
    },
    {
        "question": "What is the goal of SDG 3?",
        "options": ["Good Health and Well-being", "Gender Equality", "Affordable and Clean Energy", "Responsible Consumption"],
        "answer": "Good Health and Well-being"
    }
    # You can add more questions here...
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.current_question_index = 0
        random.shuffle(questions)  # Shuffle questions for variety

        self.question_label = tk.Label(master, text="", wraplength=300)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()
        self.options_frame = tk.Frame(master)
        self.options_frame.pack()

        self.options_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.options_frame, text="", variable=self.options_var, value="")
            button.pack(anchor='w')
            self.options_buttons.append(button)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(questions):
            question = questions[self.current_question_index]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.options_buttons[i].config(text=option, value=option)
            self.options_var.set(None)
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Quiz completed!")
            self.options_frame.pack_forget()
            self.submit_button.pack_forget()

    def check_answer(self):
        question = questions[self.current_question_index]
        if self.options_var.get() == question["answer"]:
            self.score += 1
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Incorrect! The correct answer was: {question['answer']}")

        self.current_question_index += 1
        self.master.after(2000, self.next_question)  # Wait 2 seconds before showing the next question

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SDG Educational Quiz")
    quiz_app = QuizApp(root)
    root.mainloop()
