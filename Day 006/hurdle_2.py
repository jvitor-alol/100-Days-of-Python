# Reeborg's World Hurdle 2:
from .reeborgs_world import turn_left, move, at_goal


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


while not at_goal():
    jump_hurdle()
