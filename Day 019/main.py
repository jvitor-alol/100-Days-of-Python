#!/usr/bin/env python
import turtle as t


def main() -> None:
    turtle = t.Turtle()
    screen = t.Screen()

    def move_forward() -> None:
        turtle.fd(20)

    screen.listen()
    screen.onkey(key='space', fun=move_forward)
    screen.exitonclick()


if __name__ == '__main__':
    main()
