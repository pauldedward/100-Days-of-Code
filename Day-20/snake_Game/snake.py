from turtle import Turtle

class Snake:
    def __init__(self):
        self.body = []
        for i in range (0,3):
            todd = Turtle()
            todd.penup()
            todd.color("white")
            todd.shape("square")
            todd.setx(-20 + (i * 20))
            self.body.append(todd)