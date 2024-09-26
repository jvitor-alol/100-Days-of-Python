import os
import turtle as t
from typing import TypeAlias

import pandas as pd

IMAGE = os.path.join(os.path.dirname(__file__), 'blank_states_img.gif')
STATES_DATA = os.path.join(os.path.dirname(__file__), '50_states.csv')

Coordinate: TypeAlias = tuple[float, float]


def game_setup() -> tuple[pd.DataFrame, t.Screen, t.Turtle]:
    states = pd.read_csv(STATES_DATA)

    screen = t.Screen()
    screen.title("U.S. States Game")
    screen.setup(width=750, height=500)

    screen.addshape(IMAGE)
    t.shape(IMAGE)

    marker = t.Turtle()
    marker.hideturtle()
    marker.penup()

    return states, screen, marker


def game_loop() -> None:
    states, screen, marker = game_setup()
    right_guesses = []

    while len(right_guesses) < 50:
        answer = screen.textinput(
            title=f"{len(right_guesses)}/50 States Correct",
            prompt="Guess another state name").title()

        if answer == 'Exit':
            save_missed_states(states, right_guesses)
            break

        state_coordinates = validate_state(answer, states)
        if state_coordinates and answer not in right_guesses:
            marker.goto(state_coordinates)
            marker.write(answer)
            right_guesses.append(answer)

    if len(right_guesses) == 50:
        marker.goto(-180, 0)
        marker.write("CONGRATULATIONS", font=('Courier', 30, 'normal'))
        screen.exitonclick()


def validate_state(answer: str, states: pd.DataFrame) -> Coordinate | None:
    state_record = states[states['state'] == answer]
    if not state_record.empty:
        return (state_record['x'].values[0], state_record['y'].values[0])
    else:
        return None


def save_missed_states(states: pd.DataFrame, guesses: list[str]) -> None:
    missed_states = states[~states['state'].isin(guesses)]['state']
    missed_states.to_csv(
        os.path.join(os.getcwd(), 'missed_states.csv'),
        index=False,
        header=False)
