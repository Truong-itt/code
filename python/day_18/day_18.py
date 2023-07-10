import turtle as turtle_module
import random
#cho con rua co mau
turtle_module.colormode(255)
#gan ten cho con rua
tim = turtle_module.Turtle()
#hinh dang cua con chuot
tim.shape("turtle")
tim.color("pink")
#toc do di cua con chuot
#tim.speed("fastest")
#khong hien dong di cua  cua con rua
tim.penup()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]
tim.setheading(225)
#xoat dau xuong duoi goc 255
tim.forward(300)
#di toi mot khoang 300
#huong  dau sang phai
tim.setheading(0)
bien = 100
for i in range(1,bien):
    tim.dot(24, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







#ra ra màn hinh
screen = turtle_module.Screen()
#bam bvao mot cai la tat
screen.exitonclick()