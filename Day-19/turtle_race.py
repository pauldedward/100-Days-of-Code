from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
random.shuffle(colors)

screen = Screen()
screen.setup(width=500, height=400)

todds = []


while True:
    user_bet = screen.textinput(title = "Make your Bet", prompt = "Enter turtle color :").lower()
    
    if user_bet in colors:
        is_race_on = True
        break
    else:
        print("Not valid colour, choose one from (red , green, blue, yellow, orange, purple, pink) ")


for n in range(0, 7):
    y_pos = -150 + n * 50
    todd = Turtle(shape = "turtle")
    todd.color(colors[n])
    todd.penup()
    todd.goto(-240, y_pos)
    todds.append(todd)


while is_race_on:
    
    for todd in todds:
        
        if todd.xcor() > 230:
            
            todd_color = todd.pencolor()
            if user_bet == todd_color:
                print(f"You have won!!! {todd_color} turtle won the race")
            else:
                print(f"You lost!!! {todd_color} turtle won the race")
            is_race_on = False
            
        step_size = random.randint(0,10)
        todd.forward(step_size)


screen.exitonclick()