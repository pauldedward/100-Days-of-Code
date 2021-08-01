from turtle import Turtle, Screen, heading
from snake import *
from food import *
from scoreboard import *
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("SnakeD")

snake = Snake()
food = Food()
scoreboard = Score()
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


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
# def reset():
#     tur.reset()


# screen.onkey(reset, "r")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.125)
    
    if snake.check_bitself():
        # is_game_on = False
        # break
        snake.reset_game()
        scoreboard.reset_game()
    
    snake.move(direction)
    scoreboard.show()
    
    if snake.body[0].distance(food) < 15: 
        snake.grow(direction)
        scoreboard.score += 1
        food.move()


    if snake.body[0].xcor() > 280 or snake.body[0].xcor() < -280 or snake.body[0].ycor() > 280 or snake.body[0].ycor() < -280:
        # is_game_on = False
        snake.reset_game()
        scoreboard.reset_game()

    if scoreboard.score > scoreboard.high_score:
        scoreboard.set_high_score()
        
# scoreboard.show_final()
screen.exitonclick()


# I should ve used slice ,methods and list comprehension