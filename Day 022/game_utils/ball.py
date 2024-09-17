from turtle import Turtle

from .paddles import Paddle


class Ball(Turtle):
    INITIAL_POSITION: tuple[float, float] = (0.0, 0.0)
    INITIAL_ACCELERATION: float = 0.1
    MOVE_SPEED: int = 10

    def __init__(self) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(self.INITIAL_POSITION)
        self._accel_time = self.INITIAL_ACCELERATION
        self._h_speed = self.MOVE_SPEED
        self._v_speed = self.MOVE_SPEED

    @property
    def accel_time(self) -> float:
        return self._accel_time

    @accel_time.setter
    def accel_time(self, new_accel: float) -> None:
        self._accel_time = new_accel

    @property
    def h_speed(self) -> int:
        return self._h_speed

    @h_speed.setter
    def h_speed(self, new_speed: int) -> None:
        self._h_speed = new_speed

    @property
    def v_speed(self) -> int:
        return self._v_speed

    @v_speed.setter
    def v_speed(self, new_speed: int) -> None:
        self._v_speed = new_speed

    def move(self, l_paddle: Paddle, r_paddle: Paddle, bounds: tuple) -> None:
        if self.has_hit_wall(bounds[1]):
            self.v_bounce()
        if self.has_hit_paddles(l_paddle, r_paddle):
            self.h_bounce()

        new_x = self.xcor() + self.h_speed
        new_y = self.ycor() + self.v_speed

        self.goto(new_x, new_y)

    def has_hit_wall(self, v_bounds: tuple[int, int]) -> bool:
        return not (v_bounds[0] <= self.ycor() <= v_bounds[1])

    def is_out_of_bounds(self, bounds: tuple[tuple, tuple]) -> bool:
        return not (bounds[0][0] <= self.xcor() <= bounds[0][1])

    def has_hit_paddles(self, l_paddle: Paddle, r_paddle: Paddle) -> bool:
        contact_l_pad = self.distance(l_paddle) < 50 and self.xcor() < -320
        contact_r_pad = self.distance(r_paddle) < 50 and self.xcor() > 320

        return (contact_l_pad or contact_r_pad)

    def v_bounce(self) -> None:
        self.v_speed *= -1

    def h_bounce(self) -> None:
        self.h_speed *= -1
        self.accel_time *= 0.7

    def reset_position(self) -> None:
        self.goto(self.INITIAL_POSITION)
        self.h_bounce()
        self.accel_time = self.INITIAL_ACCELERATION
