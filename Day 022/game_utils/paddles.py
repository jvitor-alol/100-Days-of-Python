from turtle import Turtle

SQUARE_SIZE_PX = 20


class Paddle(Turtle):
    WIDTH: int = 20
    HEIGHT: int = 100

    def __init__(self, x_pos_init: float, y_pos_init: float = 0) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(
            stretch_len=(self.WIDTH / SQUARE_SIZE_PX),
            stretch_wid=(self.HEIGHT / SQUARE_SIZE_PX))
        self.penup()
        self.goto(x_pos_init, y_pos_init)

    def go_up(self) -> None:
        new_y = self.ycor() + SQUARE_SIZE_PX
        self.goto(self.xcor(), new_y)

    def go_down(self) -> None:
        new_y = self.ycor() - SQUARE_SIZE_PX
        self.goto(self.xcor(), new_y)
