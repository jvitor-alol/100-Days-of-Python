#!/usr/bin/env python
import random
import sys
import turtle as t
from argparse import ArgumentParser

shapes = {
    'triangle': 3,
    'square': 4,
    'pentagon': 5,
    'hexagon': 6,
    'heptagon': 7,
    'octagon': 8,
    'nonagon': 9,
    'decagon': 10
}


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        '-o', '--option', type=int,
        choices=range(3), default=0)
    args = parser.parse_args()

    slow_moe = t.Turtle()
    slow_moe.shape('turtle')
    slow_moe.color('crimson')

    match (args.option):
        case 0:
            square_dashed_diagonal(slow_moe)
        case 1:
            different_shapes(slow_moe)
        case 2:
            random_walk(slow_moe)
        case _:
            sys.exit(1)

    my_screen = t.Screen()
    my_screen.exitonclick()


def square_dashed_diagonal(turtle: t.Turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

    turtle.left(45)
    for _ in range(7):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def different_shapes(turtle: t.Turtle):
    for sides in shapes.values():
        for _ in range(sides):
            turtle.forward(100)
            turtle.right(360 / sides)
        change_color(turtle)


def change_color(turtle: t.Turtle):
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


def random_walk(turtle: t.Turtle, iterations=200, speed=10) -> None:
    directions = [0, 90, 180, 270]
    turtle.pensize(10)
    turtle.speed(speed)
    for _ in range(iterations):
        change_color(turtle)
        turtle.setheading(random.choice(directions))
        turtle.fd(20)


if __name__ == '__main__':
    main()
