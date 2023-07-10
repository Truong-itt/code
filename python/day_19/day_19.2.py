import random
import turtle
from turtle import Turtle,Screen
screen = Screen()
screen.setup(width=500,height= 400)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race? enter a color")
danh_sach_mau =["pink","violet","black","yellow","green","blue"]
danh_sach_pos = [-70,-40,-10,20,50,80]
all_turtle =[]
# hong = Turtle(shape="turtle")

#
# hong.penup()
# hong.goto(x=-230,y=-100)

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(danh_sach_mau[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=danh_sach_pos[index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtle:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color ==  user_bet:
                print(f"you've won! the {winning_color} turtle is the winner")
            else:
                print(f"you wrong,the color winer is {winning_color}")
        bien = random.randint(0,10)
        i.forward(bien)

screen.exitonclick()
