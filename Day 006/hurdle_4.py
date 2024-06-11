# Reeborg's World Hurdle 4:
from .reeborgs_world import turn_left, move, at_goal
from .reeborgs_world import wall_in_front, front_is_clear, wall_on_right


def turn_right():
    for _ in range(3):
        turn_left()


def jump_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_hurdle()
    elif front_is_clear():
        move()
