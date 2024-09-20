from turtle import Turtle

COLOR = 'white'
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self, score: int = 0, high_score: int = 0) -> None:
        super().__init__()
        self._score = score
        self._high_score = high_score

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

    @property
    def high_score(self) -> int:
        return self._high_score

    @high_score.setter
    def high_score(self, new_score: int) -> None:
        self._high_score = new_score

    def increment_score(self) -> None:
        self.score += 1

    def display_score(self) -> None:
        text = "Score: {} High Score: {}".format(self.score, self.high_score)

        self.clear()
        self.write(text, align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        high_score = self.high_score
        score = self.score

        self.high_score = score if score > high_score else high_score
        self.score = 0
        self.display_score()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
