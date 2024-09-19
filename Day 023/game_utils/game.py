import time
import random

from turtle import Screen

from .player import Player
from .car_manager import CarManager
from .scoreboard import Scoreboard


def game_setup() -> tuple[Screen, Player, CarManager, Scoreboard]:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=player.move_up, key='Up')

    return screen, player, car_manager, scoreboard


def game_loop() -> None:
    screen, player, car_manager, scoreboard = game_setup()

    game_is_on = True
    while game_is_on:
        # generates new cars if there are fewer than 10, every 6 loops or so
        dice_roll = random.randint(1, 6)
        if dice_roll == 6 or car_manager.car_count < 10:
            for _ in range(scoreboard.game_level):
                car_manager.generate_car()

        car_manager.move_cars()

        if player.reached_finish_line():
            scoreboard.increase_level()
            car_manager.level_up()
            player.restart()

        if player.was_hit_by_car(car_manager):
            scoreboard.game_over()
            game_is_on = False

        car_manager.clear_offscreen_cars()
        # print(car_manager.car_count)
        time.sleep(0.1)
        screen.update()

    screen.exitonclick()
