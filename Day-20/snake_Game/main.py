from turtle import Turtle, Screen, heading
from snake import *
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("SnakeD")

snake = Snake()
screen.listen()
direction = 0

def move_right():
    global direction
    direction = 0
    
def move_left():
    global direction
    direction = 180

def move_up():
    global direction
    direction = 90
    
def move_down():
    global direction
    direction = 270


screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
# def reset():
#     tur.reset()
    

# screen.onkey(reset, "r")

while True:
    screen.update()
    time.sleep(.125)
    
    snake.move(direction)
    
    




screen.exitonclick()