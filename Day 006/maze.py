# Reeborg's World Maze:
from .reeborgs_world import turn_left, move, at_goal
from .reeborgs_world import front_is_clear, wall_on_right


def turn_right():
    for _ in range(3):
        turn_left()


loop_count = 0  # counts if the robot moved in circles
while not at_goal():
    if not wall_on_right() and loop_count < 4:
        turn_right()
        move()
        loop_count += 1
    elif front_is_clear():
        move()
        loop_count = 0
    else:
        turn_left()
        loop_count = 0
