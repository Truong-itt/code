import turtle as t
import random
t.colormode(255)
tim = t.Turtle()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color
tim.speed("fastest")
tim.shape("turtle")


def draw_designer(so):
    for i in range(int(360/so)):
        tim.color(random_color())
        tim.dot(24, random_color())
        tim.circle(100)
        bien = tim.heading()
        tim.setheading(bien + so)

draw_designer(5)



screen = t.Screen()
screen.exitonclick()