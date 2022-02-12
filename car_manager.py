from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        
    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

