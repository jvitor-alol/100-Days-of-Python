from turtle import Turtle

COLOR = 'white'
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self, score: int = 0) -> None:
        super().__init__()
        self._score = score

        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(x=0, y=250)
        self.display_score()

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, new_score: int) -> None:
        self._score = new_score

    def increment_score(self) -> None:
        self.score += 1

    def display_score(self) -> None:
        text = "Score: {}".format(self.score)

        self.clear()
        self.write(text, align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
