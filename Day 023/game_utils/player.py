from turtle import Turtle

from .car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color('green')
        self.shape('turtle')
        self.setheading(90)
        self.restart()

    def move_up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def reached_finish_line(self) -> bool:
        return self.ycor() >= FINISH_LINE_Y

    def was_hit_by_car(self, car_manager: CarManager) -> bool:
        for car in car_manager.car_list:
            if self.distance(car) <= 25:
                return True

    def restart(self) -> None:
        self.goto(STARTING_POSITION)
