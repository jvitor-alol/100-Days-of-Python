from turtle import Turtle

from .food import Food
from .scoreboard import Scoreboard

MOVE_DISTANCE = 20  # Snake segment size: 20x20 square
COLOR = 'white'
SHAPE = 'square'
INITIAL_BODY_LENGTH = 6
STARTING_POSITIONS = [
    (0 - MOVE_DISTANCE * idx, 0) for idx in range(INITIAL_BODY_LENGTH)
]


class Snake:
    def __init__(self) -> None:
        self._body = []
        self._body_positions = {}  # hashmap to calculate collisions
        self.create_snake_body()

        self.can_change_direction = True  # flag to prevent full turns
        self.next_move = None  # buffer to save next movement function
        self.directions = {
            90: self.snake_up,
            180: self.snake_left,
            270: self.snake_down,
            0: self.snake_right
        }

    @property
    def body(self) -> list[Turtle]:
        return self._body

    @property
    def head(self) -> Turtle:
        return self.body[0]

    @property
    def tail(self) -> Turtle:
        return self.body[-1]

    @property
    def length(self) -> int:
        return len(self.body)

    @property
    def body_positions(self) -> int:
        return self._body_positions

    def create_snake_body(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[float, float]) -> None:
        new_segment = Turtle(shape=SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)

        self.body.append(new_segment)
        self.body_positions[position] = new_segment

    def extend(self) -> None:
        self.add_segment(self.tail.position())

    def move(self) -> None:
        del self.body_positions[self.tail.position()]

        for index in range(self.length - 1, 0, -1):
            new_position = self.body[index - 1].position()
            self.body[index].goto(new_position)
            self.body_positions[new_position] = self.body[index]

        self.head.forward(MOVE_DISTANCE)
        self.body_positions[self.head.position()] = self.head

        if self.next_move is not None:
            self.next_move()
            self.next_move = None

        self.can_change_direction = True

    def change_direction(self, heading: int):
        is_opposite_dir = self.head.heading() == (heading + 180) % 360

        if self.can_change_direction and not is_opposite_dir:
            self.head.setheading(heading)
            self.can_change_direction = False
        elif not self.can_change_direction:
            self.next_move = self.directions.get(heading)

    def snake_up(self) -> None:
        self.change_direction(90)  # North: 90°

    def snake_left(self) -> None:
        self.change_direction(180)  # West: 180°

    def snake_down(self) -> None:
        self.change_direction(270)  # South: 270°

    def snake_right(self) -> None:
        self.change_direction(0)  # East: 0°

    def handle_eaten_food(self, food: Food, scoreboard: Scoreboard) -> None:
        if self.head.distance(food) < 15:
            food.refresh()
            self.extend()
            scoreboard.increment_score()
            scoreboard.display_score()

    def is_touching_body(self) -> bool:
        head_position = self.head.position()
        return self.body_positions[head_position] != self.head

    def is_out_of_bounds(self) -> bool:
        head = self.head
        bounds = {
            'x': (-280, 280),
            'y': (-280, 280)
        }

        is_xcor_in = bounds['x'][0] <= head.xcor() <= bounds['x'][1]
        is_ycor_in = bounds['y'][0] <= head.ycor() <= bounds['y'][1]

        return not (is_xcor_in and is_ycor_in)
