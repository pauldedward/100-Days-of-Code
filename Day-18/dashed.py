
from turtle import Turtle

my_turtle = Turtle()
my_screen = my_turtle.getscreen()

my_turtle.color("red")

for i in range(1, 10):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()


my_screen.exitonclick()

