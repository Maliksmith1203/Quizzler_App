from tkinter import *
from quiz_brain import QuizBrain
import data

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(height=250, width=300, bg="White")
        self.text_label = self.canvas.create_text(150, 125, width=280, text="some text", font=("Arial", 20, "italic"),
                                                  fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.score = 0
        self.score_label = Label(text=f"Score:{self.score}", bg=THEME_COLOR, fg="White", font=("Arial", 10, "bold"),
                                 pady=20)
        self.score_label.grid(row=0, column=1)

        self.true_image = PhotoImage(file="true.png")
        self.check_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(row=2, column=0, pady=20)
        self.wrong_image = PhotoImage(file="false.png")
        self.wrong_image_button = Button(image=self.wrong_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_image_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
           self.score_label.config(text=f"Score:{self.quiz.score}")
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.text_label, text=q_text)
        else:
            self.canvas.itemconfig(self.text_label,text="You reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.wrong_image_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

