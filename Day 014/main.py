#!/usr/bin/env python
import os
import random
import sys
import time
from typing import Callable

from termcolor import colored

from game_art import LOGO, VS
from game_data import DATA


def check_input(message: str, condition: Callable[[str], bool],
                message_color: str = "white") -> str:
    def clear_input_line() -> None:
        sys.stdout.write('\033[F\033[K')
        print(colored("Insert a valid value", "red"), end='', flush=True)
        time.sleep(0.5)
        for _ in range(3):
            print(colored(".", "red"), end='', flush=True)
            time.sleep(0.5)
        sys.stdout.write('\033[2K\r')

    while True:
        value: str = input(colored(message, message_color))
        try:
            satisfies_condition: bool = condition(value)
        except ValueError:
            clear_input_line()
            continue
        except Exception:
            clear_input_line()
            continue
        else:
            if satisfies_condition:
                return value
            else:
                clear_input_line()


def render_game(entities: dict, score: int) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(LOGO)
    if score > 0:
        print(f"You're right! Current score {score}")
    print(
        f"\nCompare A: {entities['A']['name']}, a "
        f"{entities['A']['description']} from {entities['A']['country']}.")
    print(VS)
    print(
        f"\nAgainst B: {entities['B']['name']}, a "
        f"{entities['B']['description']} from {entities['B']['country']}.")

    guess = check_input(
        "Who has more followers? Type 'A' or 'B': ",
        lambda x: x.upper() in ['A', 'B']).upper()
    if compare_guess(guess, entities):
        render_game(entities, score + 1)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(LOGO)
        print(f"Sorry, that's wrong. Final score: {score}")
        sys.exit()


def compare_guess(guess: str, entities: dict) -> bool:
    other_option = 'B' if guess == 'A' else 'A'
    guess_followers = entities[guess]['follower_count']
    other_followers = entities[other_option]['follower_count']

    if guess_followers > other_followers:
        entities['A'] = entities[guess]

        index_b = random.randint(0, len(DATA) - 1)
        entities['B'] = DATA[index_b]
        while entities['B']['name'] == entities['A']['name']:
            index_b = random.randint(0, len(DATA) - 1)
            entities['B'] = DATA[index_b]

        return True
    else:  # There are no two entities with the same follower count
        return False


def main() -> None:
    index_a, index_b = random.sample(range(len(DATA)), 2)
    entities = {
        'A': DATA[index_a],
        'B': DATA[index_b]
    }
    score = 0
    render_game(entities, score)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
