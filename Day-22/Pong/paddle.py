from turtle import Turtle

STEPSIZE = 40

class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)
        

    def move_up(self):
        if not self.ycor() >= 230:
            self.sety(self.ycor() + STEPSIZE)
    
    def move_down(self):
        if not self.ycor() <= -230:
            self.sety(self.ycor() - STEPSIZE)


# class ComputerPaddle:
    
#     def __init__(self, x, y):
#         super().__init__(x, y)
    
#     def move_self(self):
        