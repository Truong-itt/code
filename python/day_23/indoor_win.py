from turtle import Turtle
import random
positon=[(-220,280),(-140,280),(-60,280),(-20,280),(100,280),(180,280),(260,280)]
class indooor_win(Turtle):
    def __init__(self):
        super().__init__()
        self.door_win()
    def door_win(self):
        self.clear()
        self.shape("circle")
        # self.shapesize(1,4)
        self.color("black")
        self.penup()
        self.goto(random.choice(positon))