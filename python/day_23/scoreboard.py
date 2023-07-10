from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-240,260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level:{self.score}",align="center",font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score()
    #thong bao khi thua
    def notification_lose(self):
        self.clear()
        self.goto(0,0)
        self.write(f"your lose , your score:{self.score}", align="center", font=FONT)

    def notification(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"your win , your score:{self.score}", align="center", font=FONT)

