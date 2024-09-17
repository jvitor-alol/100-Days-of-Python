from turtle import Turtle

from .paddles import Paddle

FONT = ('Courier', 70, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()
        self._net = [
            Paddle((0, 280 - n * 80), height=40, width=10) for n in range(8)]

    def update_score(self, l_score: int = 0, r_score: int = 0) -> None:
        self.clear()
        self.goto(-100, 180)
        self.write(l_score, align=ALIGN, font=FONT)
        self.goto(100, 180)
        self.write(r_score, align=ALIGN, font=FONT)
