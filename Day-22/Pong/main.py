from turtle import Turtle, Screen
from paddle import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

player = Paddle()
screen.listen()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    # time.sleep(.125)


screen.exitonclick()
