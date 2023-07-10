from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
# t.shape("square")
# t.color("white")

s = Screen()
food = Food()

s.tracer(0)
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("my snake score")
snake = Snake()
score = Score()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")



bien = True
while bien:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.refresh_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    #detect collision with tail
    for i in snake.quan_li[1:]:
        if snake.head.distance(i) < 10:
            score.reset()
            snake.reset()
s.exitonclick()
