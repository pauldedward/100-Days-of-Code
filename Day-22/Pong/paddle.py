from turtle import Turtle

STEPSIZE = 40

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(-360, 0)
    
    def move_up(self):
        self.sety(self.ycor() + STEPSIZE)
    
    def move_down(self):
        self.sety(self.ycor() - STEPSIZE)