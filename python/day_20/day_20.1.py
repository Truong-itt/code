from turtle import Screen,Turtle
#xu lli thoi gian hoat anh tren man hinh
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
#chinh xua hoat anh cua rua cho deu lai bang thu vien co san
screen.tracer(0)

star_positions = [(0,0),(-20,0),(-40,0)]
danh_sach_quan_li=[]
for i in star_positions:
    bien = Turtle(shape="square")
    bien.color("white")
    bien.penup()
    bien.goto(i)
    danh_sach_quan_li.append(bien)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for i in range(start = 3,stop= 2,step =1) :
        bien_1 = danh_sach_quan_li[i-1].xcor()
        bien_2 = danh_sach_quan_li[i - 1].ycor()
        danh_sach_quan_li[i].goto()




#hoan thanh bam ra ngaoi dfe thoat
screen.exitonclick()