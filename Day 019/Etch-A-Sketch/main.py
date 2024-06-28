#!/usr/bin/env python
import turtle as t


def main() -> None:
    turtle = t.Turtle()
    screen = t.Screen()

    def move_forward() -> None:
        turtle.fd(10)

    def move_backwards() -> None:
        turtle.bk(10)

    def turn_left() -> None:
        turtle.left(10)

    def turn_right() -> None:
        turtle.right(10)

    screen.listen()
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='a', fun=turn_left)
    screen.onkey(key='s', fun=move_backwards)
    screen.onkey(key='d', fun=turn_right)
    screen.onkey(key='c', fun=turtle.reset)

    screen.exitonclick()


if __name__ == '__main__':
    main()
