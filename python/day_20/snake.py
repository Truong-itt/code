from turtle import Turtle
vi_tri = [(0,0),(-20,0),(-40,0)]
hang_so_di_chuyen = 20
down = 270
right = 0
left = 180
up = 90
class Snake:
    def __init__(self):
        self.quan_li = []
        self.tao_ran()
        self.head = self.quan_li[0]
    def tao_ran(self):
        for i in vi_tri:
            self.add_segment(i)
    #caác thuộc tính của con rùa và dồng tời áp nó  vào list
    def add_segment(self,i):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(i)
        self.quan_li.append(new_turtle)
    def extend(self):
        self.add_segment(self.quan_li[-1].position())
    def move(self):
        for i in range(len(self.quan_li) - 1, 0, -1):
            toa_do_x = self.quan_li[i - 1].xcor()
            toa_do_y = self.quan_li[i - 1].ycor()
            self.quan_li[i].goto(toa_do_x, toa_do_y)
        self.head.forward(hang_so_di_chuyen)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(0)
    def reset(self):
        for i in self.quan_li:
            i.goto(1000,1000)
        self.quan_li.clear()
        self.tao_ran()
        self.head = self.quan_li[0]


