from turtle import Turtle
import time
from screen import MainScreen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 15

    def move_ball(self):
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto(xcor, ycor)

    def bounce(self):
        self.y_move *= -1

    def bounce_off_a_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.bounce_off_a_paddle()
