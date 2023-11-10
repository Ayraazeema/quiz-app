from ctypes import _NamedFuncPointer
from sre_constants import _NamedIntConstant
import tkinter as tk
from unittest.mock import _NameArgsKwargs
class QuizApplication:
    def _init_(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "question": "when did Matthew Perry die ?",
                "options": ["2023", "2012", "2004", "1998"],
                "correct_option": "2023"
            },
            {
                "question": "Who is the father of python?",
                "options": ["Charles Babbage", "Dennis Ritchie", "James Gosling", "Guido Van Rossum"],
                "correct_option": "Guido Van Rossum"
            },
            {
                "question": "Where is majuli located?",
                "options": ["Gujarat", "Leh", "Assam", "kerala"],
                "correct_option": "Assam"
            }
        ]

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 14), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
                self.option_buttons[i]["state"] = "normal"

        else:
            self.display_result()

    def check_answer(self, selected_option_index):
        question_data = self.questions[self.question_index]
        selected_option = question_data["options"][selected_option_index]
        if selected_option == question_data["correct_option"]:
            self.score += 1
        self.option_buttons[selected_option_index]["state"] = "disabled"
        self.question_index += 1
        self.next_question()

    def display_result(self):
        self.question_label.config(text=f"Quiz Complete! Your Score: {self.score}/{len(self.questions)}")

if _NamedIntConstant == "_main_":
    root = tk.Tk()
    app = QuizApplication(root)
    root.mainloop()