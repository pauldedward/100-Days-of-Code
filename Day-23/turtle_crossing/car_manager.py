from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.speed(0)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
    
    def move(self, speed):
        self.goto(self.xcor() - speed, self.ycor())
    
    def check_edges(self):
        if(self.xcor() < -340):
            return True
        
    def check_collision(self, todd):
        if self.distance(todd) < 20:
            return True
