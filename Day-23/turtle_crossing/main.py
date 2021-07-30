import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MOVE_INCREMENT = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

todd = Player()
cars = [CarManager()]
score = Scoreboard()
level = 1
screen.listen()
screen.onkey(todd.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.write_level(level)
    for car in cars:
        car.move(MOVE_INCREMENT)
        if(car.check_edges()):
            cars.remove(car)
        if(car.check_collision(todd)):
            score.write_game_over()
            game_is_on = False
    
    if todd.is_at_finish():
        todd.sety(-280)
        level += 1
        MOVE_INCREMENT += 10
    if random.randint(1, 4) == 1:
        cars.append(CarManager())

screen.exitonclick()