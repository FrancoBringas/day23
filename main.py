import time
from turtle import Screen
import random
# import car_manager
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
game_is_on = True
player = Player()
scoreboard = Scoreboard()
spedd = 10
car_manager = CarManager()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ran = random.randint(1, 7)
    if ran == 6:
        car_manager.create_car()
    car_manager.move()
    if player.ycor() >= player.finish_line:
        player.goto(player.starting)
        car_manager.level_up()
        scoreboard.point()
    car_manager.move()
    screen.onkey(player.move, "Up")
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    screen.update()

screen.exitonclick()
