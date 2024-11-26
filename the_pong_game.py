"""
This program creates the famous arcade game Pong.
"""


from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(height=600, width=800)
s.bgcolor('black')
s.title("PONG")
s.tracer(0)

paddle_right = Paddle(x_coord=375, y_coord=0)
paddle_left = Paddle(x_coord=-385, y_coord=0)

ball = Ball()

score_right = Scoreboard(x_coor=200, y_coor=200)
score_left = Scoreboard(x_coor=-200, y_coor=200)

s.listen()
s.onkey(fun=paddle_right.paddle_up, key='Up')
s.onkey(fun=paddle_right.paddle_down, key='Down')
s.onkey(fun=paddle_left.paddle_up, key='w')
s.onkey(fun=paddle_left.paddle_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # Detect collision with the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.wall_bounce()

    # Detect collision with the paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 345 or ball.distance(paddle_left) < 40 and ball.xcor() < -355:
        ball.paddle_bounce()

    # Detect when the ball misses the right paddle
    if ball.xcor() > 400 and ball.distance(paddle_right) > 50:
        ball.start_again()
        score_left.update_score()

    # Detect when the ball misses the left paddle
    if ball.xcor() < -400 and ball.distance(paddle_left) > 50:
        ball.start_again()
        score_right.update_score()

s.exitonclick()
