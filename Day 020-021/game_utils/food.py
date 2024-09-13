from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self) -> None:
        rand_x, rand_y = randint(-280, 280), randint(-280, 280)
        self.goto(x=rand_x, y=rand_y)
