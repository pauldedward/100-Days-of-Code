import random
import turtle

turtle.colormode(255)
my_turtle = turtle.Turtle()
my_screen = my_turtle.getscreen()
my_turtle.speed(1)
step_size = 20
my_turtle.pensize(6)

while True:
    choice = random.randint(0, 3)
    my_turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    if choice == 0:
        my_turtle.setpos(my_turtle.xcor() + step_size, my_turtle.ycor())
    elif choice == 1:
        my_turtle.setpos(my_turtle.xcor() - step_size, my_turtle.ycor())
    elif choice == 2:
        my_turtle.setpos(my_turtle.xcor(), my_turtle.ycor() + step_size)
    elif choice == 3:
        my_turtle.setpos(my_turtle.xcor(), my_turtle.ycor() - step_size)

