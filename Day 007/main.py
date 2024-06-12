#!/usr/bin/env python
import random
import sys
import os

from termcolor import colored
from art import text2art

from utils.hangman_art import STAGES
from utils.hangman_words import WORD_LIST
from utils import check_input, is_single_letter, spinning_loader

# WORD_LIST = ["aardvark", "baboon", "camel"] # smaller word list for testing


def render_game(game_stage: str, display: list[str],
                guesses: set[str]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(text2art("hangman", font="slant")))
    if guesses:
        print(f"You've already guessed: {sorted(guesses)}")
    print(game_stage)
    print(' '.join(display) + '\n')


def player_has_won(chosen_word: str, display: list[str]) -> bool:
    if chosen_word == ''.join(display):
        return True
    else:
        return False


def main() -> None:
    chosen_word = random.choice(WORD_LIST)
    display = ['_' for _ in chosen_word]
    guesses = set()
    game_stage = STAGES.pop()
    end_of_game = False

    render_game(game_stage, display, guesses)
    while not end_of_game:
        guess = check_input("Guess a letter: ", is_single_letter).lower()
        if guess in guesses:
            spinning_loader(f'You already guessed "{guess}"!', 2, "cyan")
            render_game(game_stage, display, guesses)
            continue
        else:
            guesses.add(guess)

        for index, letter in enumerate(chosen_word):
            display[index] = guess if guess == letter else display[index]

        if guess not in chosen_word:
            spinning_loader(
                f'"{guess}" is not in the word. You lose a life!', 2, "red")
            game_stage = STAGES.pop()

        render_game(game_stage, display, guesses)
        end_of_game = player_has_won(chosen_word, display) or not STAGES

    if not STAGES:
        print(
            "The word was " +
            colored(f"{chosen_word}\nYou lost... ", "red", attrs=["blink"]))
    else:
        print(colored("You won!", "green", attrs=["blink"]))
    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
