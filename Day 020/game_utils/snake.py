from turtle import Turtle

INITIAL_BODY_LENGTH = 3
MOVE_DISTANCE = 20  # Snake segment size: 20x20 square


class Snake:
    def __init__(self) -> None:
        self._body = [
            Turtle(shape='square') for _ in range(INITIAL_BODY_LENGTH)
        ]
        self._head = self._body[0]

        for index, segment in enumerate(self._body, start=1):
            segment.penup()
            segment.color('white')
            segment.teleport(x=0 - 20 * index, y=0)

    @property
    def body(self) -> list[Turtle]:
        return self._body

    @property
    def head(self) -> Turtle:
        return self._head

    def move(self) -> None:
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].goto(self.body[index - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self) -> None:  # North: 90°
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_left(self) -> None:  # West: 180°
        if self.head.heading() != 0:
            self.head.setheading(180)

    def snake_down(self) -> None:  # South: 270°
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snake_right(self) -> None:  # East: 0°
        if self.head.heading() != 180:
            self.head.setheading(0)
