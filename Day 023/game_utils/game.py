import time

from turtle import Screen


def game_setup() -> Screen:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    return screen


def game_loop() -> None:
    screen = game_setup()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
