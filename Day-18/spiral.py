
import turtle
import random

turtle.colormode(255)
my_turtle = turtle.Turtle()
my_screen = my_turtle.getscreen()

my_turtle.speed("fastest")
circle_count = 25
tilt_angle = 360 / circle_count
angle = 0

def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


for i in range(circle_count):
    turtle.color(random_color())
    turtle.setheading(angle)
    turtle.circle(50)
    angle += tilt_angle


my_screen.exitonclick()

