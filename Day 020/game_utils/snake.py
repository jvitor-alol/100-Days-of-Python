from turtle import Turtle

INITIAL_BODY_LENGTH = 3


class Snake:
    def __init__(self) -> None:
        self._body = [
            Turtle(shape='square') for _ in range(INITIAL_BODY_LENGTH)
        ]

        for index, segment in enumerate(self._body, start=1):
            segment.penup()
            segment.color('white')
            segment.teleport(x=0 - 20 * index, y=0)

    @property
    def body(self) -> list[Turtle]:
        return self._body

    def move(self):
        raise NotImplementedError
