from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("black")

    def up(self):
        print("up")
        self.sety(self.ycor() + MOVE_DISTANCE)
    
    def is_at_finish(self):
        if self.ycor() > 280:
            return True