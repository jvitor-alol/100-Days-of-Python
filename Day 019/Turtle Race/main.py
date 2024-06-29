#!/usr/bin/env python
import random
import turtle as t

NUM_TURTLES = 6


def change_color():
    yield from ['red', 'blue', 'green', 'yellow', 'purple', 'teal']


def main() -> None:
    screen = t.Screen()
    screen.setup(width=500, height=400)

    turtles = [t.Turtle(shape='turtle') for _ in range(NUM_TURTLES)]
    colours = change_color()
    for i, turtle in enumerate(turtles):
        turtle.color(next(colours))
        turtle.penup()
        turtle.teleport(x=-230, y=-110 + 50 * i)

    bet = screen.textinput(
        title="Make a bet",
        prompt="Which turtle wins the race? Type a color: ").lower()

    turtle_race(turtles, bet)

    screen.exitonclick()


def turtle_race(turtles: list[t.Turtle], bet: str) -> None:
    is_race_over = False
    while not is_race_over:
        # Using list to consume the map and execute forward movement
        list(map(lambda x: x.forward(random.randint(1, 10)), turtles))
        if any(turtle.xcor() > 230 for turtle in turtles):
            is_race_over = True

    winning_turtle_color = max(turtles, key=lambda t: t.xcor()).pencolor()
    message = f"The {winning_turtle_color} turtle is the winner!"
    if winning_turtle_color == bet:
        print("You won! " + message)
    else:
        print("You lost... " + message)


if __name__ == '__main__':
    main()
