#!/usr/bin/env python
from turtle import Screen
import time

from game_utils import Snake


def main() -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()

    screen.listen()
    screen.onkey(key='Up', fun=snake.snake_up)
    screen.onkey(key='Left', fun=snake.snake_left)
    screen.onkey(key='Down', fun=snake.snake_down)
    screen.onkey(key='Right', fun=snake.snake_right)

    game_is_on = True
    while game_is_on:
        snake.move()
        screen.update()
        time.sleep(.05)

    screen.exitonclick()


if __name__ == '__main__':
    main()
