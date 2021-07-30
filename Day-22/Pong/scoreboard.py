from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_points = 0
        self.right_points = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.left_points, align="left", font=("Arial", 30, "normal"))
        self.goto(100, 220)
        self.write(self.right_points, align="right", font=("Arial", 30, "normal"))