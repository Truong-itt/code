from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.bien = 10
        self.many_bien = 15
        self.go_to_start()
    def move_up(self):
        bien_moi_y = self.ycor() + self.bien
        bien_moi_x = self.xcor()
        self.goto(bien_moi_x,bien_moi_y)
    def move_down(self):
        bien_moi_y = self.ycor()- self.bien
        bien_moi_x = self.xcor()
        self.goto(bien_moi_x,bien_moi_y)
    def move_right(self):
        bien_moi_y = self.ycor()
        bien_moi_x = self.xcor()+ self.many_bien
        self.goto(bien_moi_x,bien_moi_y)
    def move_left(self):
        bien_moi_y = self.ycor()
        bien_moi_x = self.xcor()- self.many_bien
        self.goto(bien_moi_x,bien_moi_y)
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(STARTING_POSITION)