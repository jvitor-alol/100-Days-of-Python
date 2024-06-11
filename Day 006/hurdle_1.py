# Reeborg's World Hurdle 1:
from .reeborgs_world import turn_left, move


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for _ in range(6):
    jump_hurdle()
