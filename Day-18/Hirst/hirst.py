# import colorgram
# colors = colorgram.extract('Day-18\Hirst\dot.jpg',10)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     c = (r,g,b)
#     color_pallette.append(c)
# print(color_pallette)

import random
import turtle

color_pallette = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143)]

turtle.colormode(255)
my_turtle = turtle.Turtle()
my_screen = my_turtle.getscreen()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed(10)
my_turtle.setpos(-250,-250)
step_size = 50

for row in range(1,11):
    for column in range(1,11):
        my_turtle.speed(2)
        my_turtle.dot(20, random.choice(color_pallette))
        
        if column < 10:
            my_turtle.forward(step_size)
    
    my_turtle.speed(10)
    my_turtle.setpos(my_turtle.xcor() - step_size * 9, my_turtle.ycor() + step_size)

my_screen.exitonclick()