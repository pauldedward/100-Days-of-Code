from turtle import Turtle

STEPSIZE = 20

class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)
        

    def move_up(self):
        if not self.ycor() >= 250:
            self.sety(self.ycor() + STEPSIZE)

    def move_down(self):
        if not self.ycor() <= -250:
            self.sety(self.ycor() - STEPSIZE)
