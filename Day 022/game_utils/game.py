import time
from turtle import Screen

from .paddles import Paddle
from .ball import Ball
from .scoreboard import Scoreboard

SQUARE_SIZE_PX = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
H_BOUNDS = (
    -(SCREEN_WIDTH) // 2 + SQUARE_SIZE_PX,
    (SCREEN_WIDTH) // 2 - SQUARE_SIZE_PX
)
V_BOUNDS = (
    -(SCREEN_HEIGHT) // 2 + SQUARE_SIZE_PX,
    (SCREEN_HEIGHT) // 2 - SQUARE_SIZE_PX
)
BOUNDS = (H_BOUNDS, V_BOUNDS)


def game_setup():
    screen = Screen()
    screen.title("Pong")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.tracer(0)

    ball = Ball()
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key='w', fun=left_paddle.go_up)
    screen.onkey(key='s', fun=left_paddle.go_down)
    screen.onkey(key='Up', fun=right_paddle.go_up)
    screen.onkey(key='Down', fun=right_paddle.go_down)

    return screen, ball, right_paddle, left_paddle, scoreboard


def game_loop() -> None:
    screen, ball, right_paddle, left_paddle, scoreboard = game_setup()

    game_is_on = True
    while game_is_on:
        ball.move(left_paddle, right_paddle, BOUNDS)
        score(ball, left_paddle, right_paddle, scoreboard)
        time.sleep(ball.accel_time)
        screen.update()

    screen.exitonclick()


def score(ball: Ball, left: Paddle, right: Paddle, sboard: Scoreboard) -> None:
    if not ball.is_out_of_bounds(bounds=BOUNDS):
        return

    if ball.xcor() > BOUNDS[0][1]:
        left.score_point()
    elif ball.xcor() < BOUNDS[0][0]:
        right.score_point()

    ball.reset_position()
    sboard.update_score(left.score, right.score)
