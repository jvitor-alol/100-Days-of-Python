from turtle import Turtle

SQUARE_SIZE_PX = 20
WIDTH: int = 20
HEIGHT: int = 100


class Paddle(Turtle):
    def __init__(
            self,
            init_pos: tuple[float, float] = (350.0, 0.0),
            width: int = WIDTH,
            height: int = HEIGHT) -> None:

        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(
            stretch_len=(width / SQUARE_SIZE_PX),
            stretch_wid=(height / SQUARE_SIZE_PX)
        )
        self.penup()
        self.goto(init_pos)
        self._score = 0

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, new_score) -> None:
        self._score = new_score

    def go_up(self) -> None:
        y_pos = self.ycor()
        new_y = (y_pos + SQUARE_SIZE_PX) if y_pos <= 220 else y_pos

        self.goto(self.xcor(), new_y)

    def go_down(self) -> None:
        y_pos = self.ycor()
        new_y = (y_pos - SQUARE_SIZE_PX) if y_pos >= -220 else y_pos

        self.goto(self.xcor(), new_y)

    def score_point(self) -> None:
        self.score += 1
