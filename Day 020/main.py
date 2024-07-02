#!/usr/bin/env python
import turtle as t
import time


def main() -> None:
    screen = t.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

    # def snake_up():
    #     snake_body[0].setheading(90)
    #     snake_body[0].forward(20)

    # def snake_left():
    #     snake_body[0].setheading(180)
    #     snake_body[0].forward(20)

    # def snake_down():
    #     snake_body[0].setheading(270)
    #     snake_body[0].forward(20)

    # def snake_right():
    #     snake_body[0].setheading(0)
    #     snake_body[0].forward(20)

    # game_is_on = True
    # while game_is_on:
    # for index, segment in enumerate(snake_body[1:]):
    #     segment.goto(snake_body[index - 1].position())
    # snake_body[0].setheading(90)
    # snake_body[0].fd(20)
    # screen.update()
    # time.sleep(1)
    # screen.listen()
    # screen.onkey(key='w', fun=snake_up)
    # screen.onkey(key='a', fun=snake_left)
    # screen.onkey(key='s', fun=snake_down)
    # screen.onkey(key='d', fun=snake_right)

    screen.exitonclick()


if __name__ == '__main__':
    main()
