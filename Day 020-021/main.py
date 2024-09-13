#!/usr/bin/env python
from turtle import Screen
import time

from game_utils import Snake, Food, Scoreboard


def main() -> None:
    screen = Screen()
    snake, food, scoreboard = game_setup(screen)

    game_loop(
        snake=snake,
        food=food,
        s=screen,
        score=scoreboard,
    )
    screen.exitonclick()


def game_loop(snake: Snake, food: Food, s: Screen, score: Scoreboard) -> None:
    game_is_on = True
    while game_is_on:
        snake.move()
        snake.handle_eaten_food(food, score)
        s.update()
        time.sleep(.1)

        if snake.is_out_of_bounds() or snake.is_touching_body():
            score.game_over()
            game_is_on = False


def game_setup(screen: Screen) -> tuple[Snake, Food, Scoreboard]:
    screen.title("Snake Game")
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key='Up', fun=snake.snake_up)
    screen.onkey(key='Left', fun=snake.snake_left)
    screen.onkey(key='Down', fun=snake.snake_down)
    screen.onkey(key='Right', fun=snake.snake_right)

    return snake, food, scoreboard


if __name__ == '__main__':
    main()
