import random
from turtle import Turtle

my_turtle = Turtle()
my_screen = my_turtle.getscreen()
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "grey", "brown"]

my_turtle.penup()
my_turtle.goto(-50, 50)
my_turtle.pendown()

for sides in range(3,11):
    my_turtle.color(random.choice(colors))
    for turns in range(sides):
        angle = 360 / sides
        my_turtle.forward(100)
        my_turtle.right(angle)


my_screen.exitonclick()

