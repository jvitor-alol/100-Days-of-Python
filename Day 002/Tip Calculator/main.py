#!/usr/bin/env python
import sys
import time

from termcolor import colored

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number.
# You might have to do some Googling to solve this.💪

# Write your code below this line 👇


def clear_previous_line() -> None:
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')


def value_input(message: str) -> int:
    while True:
        try:
            value = int(input(message))
        except ValueError:
            clear_previous_line()
            print("\033[31mInsert a valid value", end='', flush=True)
            time.sleep(0.5)
            for _ in range(3):
                print(".", end='', flush=True)
                time.sleep(0.5)
            else:
                sys.stdout.write('\033[2K\r')
        else:
            return value


def main() -> None:
    print(colored(
        "{} Welcome to \033[9mjust\033[29m the tip calculator {}\n"
        .format(*(["*" * 10]*2)),
        color="light_red",
        attrs=["bold", "blink"])
    )

    bill = value_input(colored("What was the total bill? $ ", "blue"))
    tip = value_input(colored(
        "How much tip would you like to give? 10, 12, or 15? ", "blue"))
    num_people = value_input(
        colored("How many people to split the bill? ", "blue"))

    individual_bill = (bill * (1 + tip / 100)) / num_people
    print(
        "\033[36mEach person should pay: "
        f"\033[33m$ {individual_bill:.2f}\033[0m")


if __name__ == '__main__':
    main()
