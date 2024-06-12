#!/usr/bin/env python
import random
import sys
import time
import os
import re
from typing import Any, Callable

from termcolor import colored
from art import text2art

WORD_LIST = ["aardvark", "baboon", "camel"]

STAGES = [
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

# Step 1
# TODO-1 - Randomly choose a word from the word_list and assign it to a
# variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a
# variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters
# in the chosen_word.

# Step 2
# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be
# ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in
# the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display
# should be ["_", "p", "p", "_", "_"].
# TODO-3: - Print 'display' and you should see the guessed letter in the
# correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter.
# We'll tackle that in step 3.

# Step 3
# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the
# chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

# Step 4
# TODO-1: - Create a variable called 'lives' to keep track of the
# number of lives left.
# Set 'lives' to equal 6.
# TODO-2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print
# "You lose."
# TODO-3: - print the ASCII art from 'stages' that corresponds to
# the current number of 'lives' the user has remaining.


def render_game(game_stage: str, display: list[str]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(text2art("hangedman", font="slant")))
    print(game_stage)
    print(' '.join(display) + '\n')


def player_has_won(chosen_word: str, display: list[str]) -> bool:
    if chosen_word == ''.join(display):
        return True
    else:
        return False


def three_dots_message(message: str, color_option: str) -> None:
    print(colored(message, color_option), end='', flush=True)
    time.sleep(0.5)
    for _ in range(3):
        print(colored(".", color_option), end='', flush=True)
        time.sleep(0.5)
    sys.stdout.write('\033[2K\r')  # Clears line


def clear_previous_line() -> None:
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')


def is_single_letter(value: str) -> bool:
    if re.match("^[a-zA-Z]$", value):
        return True
    else:
        return False


def check_input(message: str, message_color: str,
                condition: Callable[[Any], bool]) -> Any:
    while True:
        value = input(colored(message, message_color)).lower()
        if condition(value):
            return value
        clear_previous_line()
        three_dots_message("Insert a valid value", "red")


def main() -> None:
    chosen_word = random.choice(WORD_LIST)
    display = ['_' for _ in chosen_word]
    end_of_game = False
    game_stage = STAGES.pop()
    render_game(game_stage, display)

    # Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    while not end_of_game:
        guess = check_input("Guess a letter: ", "white", is_single_letter)

        for index, letter in enumerate(chosen_word):
            display[index] = guess if guess == letter else display[index]

        if guess not in chosen_word:
            game_stage = STAGES.pop()

        render_game(game_stage, display)
        end_of_game = player_has_won(chosen_word, display) or not STAGES

    if not STAGES:
        print("You lost.")
    else:
        print("You won.")

    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
