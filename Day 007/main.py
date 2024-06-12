#!/usr/bin/env python
import random

word_list = ["aardvark", "baboon", "camel"]

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


def main() -> None:
    chosen_word = random.choice(word_list)
    display = ['_' for _ in chosen_word]

    # Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    guess = input("Guess a letter: ").lower()

    for index, letter in enumerate(chosen_word):
        display[index] = guess if guess == letter else display[index]

    print(' '.join(display))


if __name__ == '__main__':
    main()
