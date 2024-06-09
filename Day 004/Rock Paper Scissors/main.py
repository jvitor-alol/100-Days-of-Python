#!/usr/bin/env python
import random

ROCK_ART = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER_ART = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS_ART = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

CHOICES = [
    {'name': 'rock', 'art': ROCK_ART},
    {'name': 'paper', 'art': PAPER_ART},
    {'name': 'scissors', 'art': SCISSORS_ART},
]

WIN_CONDITIONS = [(0, 2), (1, 0), (2, 1)]
TIE_CONDITIONS = [(0, 0), (1, 1), (2, 2)]
LOSE_CONDITIONS = [(0, 1), (1, 2), (2, 0)]


def get_player_choice() -> int:
    while True:
        try:
            choice = int(input(
                "What do you choose? "
                "Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")


def main() -> None:
    player_choice = get_player_choice()
    print(CHOICES[player_choice]['art'])

    cpu_choice = random.randint(0, 2)
    print("Computer chose: {}\n{}".format(
        CHOICES[cpu_choice]['name'], CHOICES[cpu_choice]['art']))

    game_evaluation = (player_choice, cpu_choice)
    if game_evaluation in WIN_CONDITIONS:
        print("You won!")
    elif game_evaluation in TIE_CONDITIONS:
        print("It's a tie.")
    elif game_evaluation in LOSE_CONDITIONS:
        print("You lose.")


if __name__ == '__main__':
    main()
