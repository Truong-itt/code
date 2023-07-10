from turtle import Turtle
alignment = "center"
FONT = ("Courier", 22, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.bien = -1
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
        self.refresh_score()
    def update_score(self):
        self.clear()
        self.write(f"score: {self.bien} high score: {self.high_score}",align=alignment, font=FONT)
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"game over", align=alignment, font=FONT)
    def refresh_score(self):
        self.bien += 1
        self.clear()
        self.update_score()
    def reset(self):

        if self.bien > self.high_score:
            self.high_score = self.bien
        self.bien =0
        self.update_score()
