
from turtle import Turtle

my_turtle = Turtle()
my_screen = my_turtle.getscreen()

my_turtle.color("red")

for i in range(1, 5):
    my_turtle.forward(100)
    my_turtle.right(90)


my_screen.exitonclick()

