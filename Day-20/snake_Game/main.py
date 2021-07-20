from turtle import Turtle, Screen, heading
from snake import *
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("SnakeD")

snake = Snake()
screen.update()
direction = 0

while True:
    snake.move(direction)
    time.sleep(.25)
    screen.update()





screen.exitonclick()