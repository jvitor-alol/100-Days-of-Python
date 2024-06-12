#!/usr/bin/env python
import random

# Step 1
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a
# variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a
# variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters
# in the chosen_word.


def main() -> None:
    chosen_word = random.choice(word_list)
    guess = input("Guess a letter: ").lower()

    [print(guess == letter) for letter in chosen_word]


if __name__ == '__main__':
    main()
