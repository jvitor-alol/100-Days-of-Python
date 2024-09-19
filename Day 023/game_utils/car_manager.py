import random
from turtle import Turtle

COLORS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DANGER_ZONE = (-250, 250)


class Car(Turtle):
    def __init__(self, x_pos: int = 320) -> None:
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        # x_cor at the edge of the screen: 320
        self.goto(x_pos, random.randint(DANGER_ZONE[0], DANGER_ZONE[1]))

    def move(self, level: int = 1) -> None:
        speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1)
        self.backward(speed)


class CarManager:
    def __init__(self) -> None:
        self._car_list: list[Car] = []
        self._level = 1

    @property
    def car_list(self) -> list[Car]:
        return self._car_list

    @car_list.setter
    def car_list(self, new_list: list[Car]) -> None:
        self._car_list = new_list

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, new_level: int) -> None:
        self._level = new_level

    @property
    def car_count(self) -> int:
        return len(self.car_list)

    def level_up(self) -> None:
        self.level += 1

    def generate_car(self) -> None:
        new_car = Car()
        self.car_list.append(new_car)

    def clear_offscreen_cars(self) -> None:
        for car in self.car_list:
            if car.xcor() < -320:
                car.hideturtle()

        self.car_list = list(filter(lambda c: c.xcor() >= -320, self.car_list))

    def move_cars(self) -> None:
        for car in self.car_list:
            car.move(self.level)
