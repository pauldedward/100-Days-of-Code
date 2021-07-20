from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()

        self.speed(0)
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_len=.75, stretch_wid=.75)
        self.penup()
        
        self.move()
        
    def move(self):
        
        x = random.randint( -280, 280)
        y = random.randint( -280, 280) 
        self.goto(x, y)