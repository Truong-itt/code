from turtle import Turtle
import random
colour = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#cau hỏi dặt ra là lam sao tạo ra nhieu paddle va co the di chuyen random
#co logicc voi nhau duoc

class CarManager(Turtle):
    def __init__(self):
        #tạo ra một list các xe hoi
        self.all_car=[]
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_change = random.randint(1,6)
        if random_change == 2:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(colour))
            random_y = random.randint(-250,263)
            new_car.goto(300,random_y)
            self.all_car.append(new_car)
    #di chuyen cac o to hay noi cach khac la duy chuyen con rau
    def move_cars(self):
        for i in self.all_car:
            i.backward(self.car_speed)
    def level_up(self):
        self.car_speed *= 1.39