#!/usr/bin/env python
import os
import random
import sys
import time
from typing import Callable

from art import text2art
from termcolor import colored

LOGO = colored(
    text2art("Guess the Number", font='tarty7'),
    "green", attrs=["blink"])
HARD_MODE = 5  # Only 5 turns to guess
EASY_MODE = 10  # 10 guesses


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


def set_difficulty() -> int:
    difficulty = check_input(
        "Choose a difficulty. Type 'easy' or 'hard': ",
        lambda x: x.lower() in ['easy', 'hard']).lower()

    if difficulty == 'easy':
        return EASY_MODE
    elif difficulty == 'hard':
        return HARD_MODE


def play_game(num_tries: int, secret_num: int) -> bool:
    print()  # Skip a line for visuals

    def attempts_generator():
        yield from ('1st', '2nd', '3rd')
        yield from (f"{x}th" for x in range(4, 11))

    attempts = attempts_generator()
    while num_tries > 0:
        print(f"You have {num_tries} attempts remaining to guess the number.")
        guess = int(check_input("Make a guess: ",
                    lambda x: int(x) in range(1, 101)))

        if guess == secret_num:
            return True
        elif guess > secret_num:
            sys.stdout.write('\033[F\033[K\033[F\033[K')
            print(f"({next(attempts)}) {guess} is too \033[31;1mhigh\033[0m!")
        else:
            sys.stdout.write('\033[F\033[K\033[F\033[K')
            print(f"({next(attempts)}) {guess} is too \033[34;1mlow\033[0m!")

        num_tries -= 1
    return False


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(LOGO)
    print(
        "\nWelcome to the Number Guessing Game!\n"
        "I'm thinking of a number between 1 and 100.")

    secret_num = random.randint(1, 100)
    turns = set_difficulty()

    if play_game(turns, secret_num):
        print(f"\nYou got it! The answer was {secret_num}")
    else:
        print(f"\nYou've run out of guesses, you lose. Answer: {secret_num}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
