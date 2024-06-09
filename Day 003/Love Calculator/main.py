#!/usr/bin/env python
import time


def calculate_score(name1: str, name2: str) -> int:
    true_word = ["T", "R", "U", "E"]
    love_word = ["L", "O", "V", "E"]

    combined_names = name1 + name2

    truelove_filter = (
        len(list(filter(lambda x: x in true_word, combined_names))),
        len(list(filter(lambda x: x in love_word, combined_names)))
    )

    return 10 * truelove_filter[0] + truelove_filter[1]


def main() -> None:
    print("****** Welcome to The \033[31mLOVE\033[0m Calculator ******\n")
    name1 = input("# What is your name? ")
    name2 = input("# What is their name? ")

    print("The Love Calculator is calculating your score", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(.5)
    else:
        print()

    score = calculate_score(name1.upper(), name2.upper())

    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score > 40 and score < 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")


if __name__ == '__main__':
    main()
