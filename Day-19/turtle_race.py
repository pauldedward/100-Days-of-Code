from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "grey", "brown"]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title = "Make your Bet", prompt = "Enter turtle color :").lower()

todds = []

for n in range(0, 7):
    y_pos = -150 + n * 50
    todd = Turtle(shape = "turtle")
    todd.color(random.choice(colors))
    todd.penup()
    todd.goto(-240, y_pos)
    todd.pendown()
    todds.append(todd)






screen.exitonclick()