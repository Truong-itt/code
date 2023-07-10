from turtle import  Screen,Turtle
from paddle import paddle_new
from ball import ball_new
import  time
from score_pong import score_pong

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)

t_right = paddle_new((350,0))
t_leight = paddle_new((-350,0))
score_pong = score_pong()


ball = ball_new()

#cho máy nghe lânhj mình cài đăt
screen.listen()
screen.onkey(t_right.go_up,"Up")
screen.onkey(t_right.go_down,"Down")

screen.onkey(t_leight.go_up,"w")
screen.onkey(t_leight.go_down,"s")

variable = True
while variable:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    # xu li khi va vao truong
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # xu li khi va vao vao thanh paddle
    if ball.distance(t_right) < 50 and ball.xcor() > 320 or ball.distance(t_leight) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #xu li khi va vao thanh ben trai
    #khi thanh nay ma cham duo thanh thi
    if ball.xcor() > 380:
        ball.reset_pos()
        score_pong.l_point()
    #xu li khi va vao thanh ben phai
    if ball.xcor() < -380:
        ball.reset_pos()
        score_pong.r_point()
screen.exitonclick()
