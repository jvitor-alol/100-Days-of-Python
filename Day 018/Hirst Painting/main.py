#!/usr/bin/env python
import random
import turtle as t

import colorgram as cg

NUM_COLORS = 41  # 40 dots plus background
START_POS = (-240, -220)  # Starting position for centered 10x10 grid


def main() -> None:
    colours = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in hirst_colors()]

    t.colormode(255)  # Change RGB mode to 8 bits
    screen = t.Screen()
    turtle = t.Turtle()
    turtle.penup()
    turtle.teleport(*START_POS)

    draw_hirst_painting(turtle, colours)

    screen.exitonclick()


def hirst_colors() -> list[cg.Color]:
    return cg.extract('./hirst_sample.jpg', NUM_COLORS)


def draw_hirst_painting(
        turtle: t.Turtle, colours: list[tuple[int]],
        grid_rows: int = 10, grid_columns: int = 10) -> None:
    turtle.hideturtle()
    for row in range(1, grid_rows + 1):
        for _ in range(grid_columns):
            turtle.dot(20, random.choice(colours))
            turtle.fd(50)
        turtle.teleport(START_POS[0], START_POS[1] + 50 * row)


if __name__ == '__main__':
    main()
