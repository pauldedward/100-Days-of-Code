from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(-200, 250)

    def write_level(self, level):
        self.clear()
        self.write(f"Level : {level}", align="center", font=FONT)

    def write_game_over(self):
        self.goto(0,0)
        self.write("Game_Over", align="center", font=FONT)