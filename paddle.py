"""
This program contains the paddle class that controls all the paddle-related functionality.
"""

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coord, y_coord):
        super().__init__()

        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_coord, y=y_coord)

    def paddle_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def paddle_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
