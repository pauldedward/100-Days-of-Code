from turtle import Turtle, Screen
from paddle import *
from ball import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

paddle_l = Paddle(350, 0)
paddle_r = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(paddle_l.move_up, "Up")
screen.onkey(paddle_l.move_down, "Down")

screen.onkey(paddle_r.move_up, "w")
screen.onkey(paddle_r.move_down, "s")

is_game_on = True
sleep_time = 0.09

while is_game_on:
    screen.update()
    score.write_score()
    ball.move()
    ball.bounce()

    if ball.xcor() >= 320:
        if(ball.collide(paddle_l, -20)):
            sleep_time -= .01;
    elif ball.xcor() <= -320:
        if(ball.collide(paddle_r, 20)):
            sleep_time -= .01;
    
    if ball.xcor() > 400:
        score.left_points += 1
        ball.goto(0,0)
        ball.x_step *= -1
        sleep_time = .09
    elif ball.xcor() < -400:
        score.right_points += 1
        ball.goto(0,0)
        ball.x_step *= -1
        sleep_time = .09

    if sleep_time <= 0:
        sleep_time = .01
    time.sleep(sleep_time)
screen.exitonclick()
