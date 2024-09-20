from turtle import Turtle

from .food import Food
from .scoreboard import Scoreboard

MOVE_DISTANCE = 20  # Snake segment size: 20x20 square
COLOR = 'green'
SHAPE = 'square'
INITIAL_BODY_LENGTH = 3
STARTING_POSITIONS = [
    (0 - MOVE_DISTANCE * idx, 0) for idx in range(INITIAL_BODY_LENGTH)
]


class Snake:
    def __init__(self) -> None:
        self._body = []
        # hashmap to calculate collisions (NOT WORKING)
        # self._body_positions = {}
        self.create_snake_body()

        self.can_change_direction = True  # flag to prevent full turns
        self.next_move = None  # buffer to save next movement function

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

    # @property
    # def body_positions(self) -> int:
    #     return self._body_positions

    def create_snake_body(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[float, float]) -> None:
        new_segment = Turtle(shape=SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)

        self.body.append(new_segment)
        # self.body_positions[position] = new_segment

    def extend(self) -> None:
        self.add_segment(self.tail.position())

    def move(self) -> None:
        # del self.body_positions[self.tail.position()]
        if self.next_move is not None:
            self.next_move()
            self.next_move = None

        for index in range(self.length - 1, 0, -1):
            new_position = self.body[index - 1].position()
            self.body[index].goto(new_position)
            # self.body_positions[new_position] = self.body[index]

        self.head.forward(MOVE_DISTANCE)
        # self.body_positions[self.head.position()] = self.head

        self.can_change_direction = True

    def change_direction(heading: int) -> None:
        def dir_decorator(func):
            def wrapper(self, *args, **kwargs):
                is_opposite_dir = self.head.heading() == (heading + 180) % 360

                if not self.can_change_direction:
                    self.next_move = func.__get__(self)
                elif self.can_change_direction and not is_opposite_dir:
                    self.head.setheading(heading)
                    self.can_change_direction = False

                return func(self, *args, **kwargs)
            return wrapper
        return dir_decorator

    @change_direction(90)  # North: 90°
    def snake_up(self) -> None:
        pass

    @change_direction(180)  # West: 180°
    def snake_left(self) -> None:
        pass

    @change_direction(270)  # South: 270°
    def snake_down(self) -> None:
        pass

    @change_direction(0)  # East: 0°
    def snake_right(self) -> None:
        pass

    def handle_eaten_food(self, food: Food, scoreboard: Scoreboard) -> None:
        if self.head.distance(food) < 15:
            food.refresh()
            self.extend()
            scoreboard.increment_score()
            scoreboard.display_score()

    def is_touching_body(self) -> bool:
        for segment in self.body[1:]:
            if self.head.distance(segment) < 10:
                return True

    def is_out_of_bounds(self) -> bool:
        head = self.head
        bounds = {
            'x': (-280, 280),
            'y': (-280, 280)
        }

        is_xcor_in = bounds['x'][0] <= head.xcor() <= bounds['x'][1]
        is_ycor_in = bounds['y'][0] <= head.ycor() <= bounds['y'][1]

        return not (is_xcor_in and is_ycor_in)

    def reset(self) -> None:
        self.hidesnake()
        self.body.clear()

        self.create_snake_body()

    def hidesnake(self) -> None:
        for segment in self.body:
            segment.hideturtle()
