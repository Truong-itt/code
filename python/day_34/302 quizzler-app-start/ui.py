THEME_COLOR = "#375362"
déighner = ('Arial',20,'italic')
from tkinter import *
from quiz_brain import QuizBrain
#sử dụng giao diện dồ hoạ cho bài này
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz =quiz_brain
        self.window =Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        bien = PhotoImage(file='images/false.png')
        bien_2 = PhotoImage(file='images/true.png')
        # self.canvas = Canvas(width=300,height=250)
        # lam hai cai nut cho may
        self.unknown_button =Button(image=bien,highlightthickness=0,command=self.false_passed)
        self.unknown_button.grid(row=2, column=1)
        self.known_button =Button(image=bien_2,highlightthickness=0.,command=self.true_passed)
        self.known_button.grid(row=2, column=0)
        #TOẠ CAI TÍNH DIỂM BĂNG THUỘC TÍNH LABEL
        self.score_lable = Label(text='Score: 0',fg='white',bg=THEME_COLOR)
        self.score_lable.grid(row=0,column=1)
        #tạo khung chứ nội dung câu chuyện muốn tunhưu chiện
        self.canvas = Canvas(width=300,height=250,bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='Some the question text',
            fill=THEME_COLOR,
            font = déighner)

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='yoe are reached the end of the quizz')
            self.unknown_button.config(state='disabled')
            self.known_button.config(state='disabled')
    #sư lí truyên dẽ liệu đúng sai
    def true_passed(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)
    def false_passed(self):
        is_right=self.quiz.check_answer('False')
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        print(type(is_right))
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)