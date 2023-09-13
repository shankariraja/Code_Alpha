import tkinter as tk
import random

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400") 

        self.questions = []
        self.score = 0
        self.current_question_index = 0

        # Create and configure labels
        self.question_label = tk.Label(root, text="", wraplength=600, font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i),font=("Helvetica", 14))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        # Add questions
        self.add_question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
        self.add_question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Venus"], "Jupiter")
        self.add_question("Who wrote the play 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], "William Shakespeare")

        self.thank_you_label = tk.Label(root, text="Thank you for attending!", font=("Helvetica", 16))  # Thank you message
        self.thank_you_label.pack()

        # Hide the thank you label initially
        self.thank_you_label.pack_forget()
        
    def add_question(self, question, options, correct_answer):
        self.questions.append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        })

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['question'])
        for i, button in enumerate(self.option_buttons):
            button.config(text=question_data['options'][i])

    def check_answer(self, selected_index):
        question_data = self.questions[self.current_question_index]
        if question_data['options'][selected_index] == question_data['correct_answer']:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.result_label.config(text=f"Your score: {self.score}/{len(self.questions)}")
        self.result_label.pack()
        self.thank_you_label.pack()

def main():
    root = tk.Tk()
    quiz = Quiz(root)
    quiz.display_question()
    root.mainloop()

if __name__ == "__main__":
    main()
