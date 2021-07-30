from turtle import Turtle, xcor
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__() 
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.initial_velocity = (random.randint(0, 1), random.randint(0, 1))
        self.x_step =  10 if self.initial_velocity[0] else -10
        self.y_step =  10 if self.initial_velocity[1] else -10
        print(self.x_step, self.y_step)
    
    def move(self):
        
        self.goto(self.xcor() + self.x_step, self.ycor() + self.y_step)
    
    def bounce(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_step = self.y_step * -1
    
    def collide(self, paddle, xoff):
        x_collision = paddle.xcor() + xoff
        y_pos = paddle.ycor()
        
        if self.xcor() == x_collision:
            if self.ycor() <= y_pos + 50 and self.ycor() >= y_pos - 50:
                self.x_step = self.x_step * -1
                return True
