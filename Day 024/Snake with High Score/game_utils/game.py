import time
import os
from turtle import Screen

from .snake import Snake
from .food import Food
from .scoreboard import Scoreboard


SETTINGS = {
    'easy': 0.1,
    'normal': 0.08,
    'hard': 0.06,
    'very hard': 0.09
}
HIGH_SCORE_FILE = os.path.join(os.getcwd(), 'high_score.txt')


def game_loop(difficulty: str) -> None:
    screen, snake, food, scoreboard = game_setup()

    game_is_on = True
    while game_is_on:
        snake.move()
        snake.handle_eaten_food(food, scoreboard)
        screen.update()

        if difficulty != 'very hard':
            time.sleep(SETTINGS.get(difficulty))
        else:
            time.sleep(SETTINGS.get(difficulty) - 0.01 * snake.length)

        if snake.is_out_of_bounds() or snake.is_touching_body():
            scoreboard.reset()
            set_high_score(scoreboard.high_score)
            snake.reset()
            # game_is_on = False

    screen.exitonclick()


def game_setup() -> tuple[Screen, Snake, Food, Scoreboard]:
    screen = Screen()
    screen.title("Snake Game")
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(high_score=get_high_score())

    screen.listen()
    screen.onkey(key='Up', fun=snake.snake_up)
    screen.onkey(key='Left', fun=snake.snake_left)
    screen.onkey(key='Down', fun=snake.snake_down)
    screen.onkey(key='Right', fun=snake.snake_right)

    return screen, snake, food, scoreboard


def get_high_score() -> int:
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    with open(HIGH_SCORE_FILE, 'r', encoding='utf-8') as file:
        return int(file.readline())


def set_high_score(high_score: int) -> None:
    current_high_score = get_high_score()
    if high_score <= current_high_score:
        return
    with open(HIGH_SCORE_FILE, 'w', encoding='utf-8') as file:
        file.write(str(high_score))