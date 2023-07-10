from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()
def huong_len():
    tim.forward(10)
def huong_xuong():
    tim.backward(10)
def xang_trai():
    bien = tim.heading() +10
    tim.setheading(bien)
def xang_phai():
    bien = tim.heading() - 10
    tim.setheading(bien)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.setheading(90)
    tim.pendown()
tim.setheading(90)
screen.listen()
# screen.onkey(key="space",fun=huong_len)
screen.onkey(key="w",fun=huong_len)
screen.onkey(key="a",fun=xang_trai)
screen.onkey(key="s",fun=huong_xuong )
screen.onkey(key="d",fun=xang_phai)
screen.onkey(key="c",fun=clear)

# screen.onkey(key="space",fun=huong_xuong)
# screen.onkey(key="space",fun=xang_trai)
# screen.onkey(key="space",fun=xang_phai)
screen.exitonclick()