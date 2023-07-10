import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from indoor_win import indooor_win

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager=CarManager()
score = Scoreboard()
indoor_win =indooor_win()
indoor_win.door_win()
screen.listen()
screen.onkey(turtle.move_up,"Up")
screen.onkey(turtle.move_down,"Down")
screen.onkey(turtle.move_right,"Right")
screen.onkey(turtle.move_left,"Left")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_car:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.notification_lose()
    if turtle.is_at_finish_line():
        if indoor_win.distance(turtle) < 20:
            score.increase_score()
            turtle.go_to_start()
            indoor_win.door_win()
            car_manager.level_up()
        else:
            game_is_on = False
            score.notification_lose()



screen.exitonclick()