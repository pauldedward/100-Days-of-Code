from turtle import *

class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.goto(-20,260)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.show()
        
    
    def show(self):
        self.clear()
        self.write(f"Score: {self.score}",align ="center", font=("Arial",20,"normal"))
    
    def show_final(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!",align ="center", font=("Arial",28,"normal"))