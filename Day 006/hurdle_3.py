# Reebord's World Hurdle 3:
from .reeborgs_world import turn_left, move
from .reeborgs_world import wall_in_front, front_is_clear, at_goal


def turn_right():
    for _ in range(3):
        turn_left()


def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_hurdle()
    elif front_is_clear():
        move()
