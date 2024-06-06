#!/usr/bin/env python
from art import text2art
from termcolor import colored

# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end


def main() -> None:
    print(colored(
        "##################### hello friend #####################\n",
        "green", attrs=["bold", "blink"]))

    pet_name = input(
        "What's your {}?\n"
        .format(colored("pet's name", "red", attrs=["blink", "bold"])))
    funny_word = input(
        "What's a {} you find {}?\n"
        .format(colored("word", "red", attrs=["blink", "bold"]),
                colored("funny", "red", attrs=["blink", "bold"])))

    print(colored(
        "\nYou should name your band:\n",
        "green", attrs=["bold", "blink"]))
    art = text2art(pet_name.upper() + funny_word.upper(), font="random")
    print(colored(art, "red", "on_black", attrs=["blink"]))


if __name__ == '__main__':
    main()
