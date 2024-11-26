"""
This program contains the ball class that controls all the ball-related functionality.
"""


from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def start_again(self):
        self.home()
        self.paddle_bounce()
        self.move_speed = 0.1
