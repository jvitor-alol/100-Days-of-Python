from turtle import Screen

from .paddles import Paddle


def game_setup():
    screen = Screen()
    screen.title("Pong")
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.tracer(0)

    right_paddle = Paddle(350)
    left_paddle = Paddle(-350)

    screen.listen()
    screen.onkey(key='w', fun=left_paddle.go_up)
    screen.onkey(key='s', fun=left_paddle.go_down)
    screen.onkey(key='Up', fun=right_paddle.go_up)
    screen.onkey(key='Down', fun=right_paddle.go_down)

    return screen


def game_loop() -> None:
    screen = game_setup()

    game_is_on = True
    while game_is_on:
        screen.update()

    screen.exitonclick()
