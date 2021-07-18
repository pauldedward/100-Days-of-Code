import random
from turtle import Turtle

my_turtle = Turtle()
my_screen = my_turtle.getscreen()
my_turtle.speed(1)
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black", "grey", "brown"]

step_size = 20
my_turtle.pensize(6)

while True:
    choice = random.randint(0, 3)
    my_turtle.color(random.choice(colors))
    
    if choice == 0:
        my_turtle.setpos(my_turtle.xcor() + step_size, my_turtle.ycor())
    elif choice == 1:
        my_turtle.setpos(my_turtle.xcor() - step_size, my_turtle.ycor())
    elif choice == 2:
        my_turtle.setpos(my_turtle.xcor(), my_turtle.ycor() + step_size)
    elif choice == 3:
        my_turtle.setpos(my_turtle.xcor(), my_turtle.ycor() - step_size)

