"""
This program contains the Scoreboard class that controls all score-related functionality.
"""


from turtle import Turtle

FONT = ('Courier', 100, 'normal')


class Scoreboard(Turtle):
    def __init__(self, x_coor, y_coor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=x_coor, y=y_coor)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", False, 'center', FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
