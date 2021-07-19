from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    tur.forward(10)
    
def move_backward():
    tur.backward(10)

def turn_left():
    angle = tur.heading()
    tur.setheading(angle - 10)
    
def turn_right():
    angle = tur.heading()
    tur.setheading(angle + 10)

def reset():
    tur.reset()
    
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(reset, "r")

screen.exitonclick()
