from turtle import *



class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.goto(-20,260)
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("./Day-20&21&24/snake_Game/high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.show()
        
    
    def show(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
    
    # def show_final(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!!!",align ="center", font=("Arial",28,"normal"))
    
    def set_high_score(self):
        self.high_score = self.score
        with open("./Day-20&21&24/snake_Game/high_score.txt", mode="w") as high_score:
            high_score.write(f"{self.high_score}")
    
    
    def reset_game(self):
        self.score = 0