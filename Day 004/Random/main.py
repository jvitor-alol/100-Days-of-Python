#!/usr/bin/env python
import random
import argparse

import my_module


def func_1() -> None:
    random_int = random.randint(1, 10)
    print(random_int)

    print(f"Pi = {my_module.PI}")

    random_number = random.randint(1, 100) * random.random()
    print(random_number)


def func_2() -> None:
    states_of_us = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                    "Connecticut", "Massachusetts", "Maryland",
                    "South Carolina", "New Hampshire", "Virginia", "New York",
                    "North Carolina", "Rhode Island", "Vermont", "Kentucky",
                    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
                    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                    "California", "Minnesota", "Oregon", "Kansas",
                    "West Virginia", "Nevada", "Nebraska", "Colorado",
                    "North Dakota", "South Dakota", "Montana", "Washington",
                    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                    "Arizona", "Alaska", "Hawaii"]
    dirty_dozen = [
        "Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
        "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
        "Celery", "Potatoes"]

    # random.seed(1000)
    index = random.randint(0, 49)

    print(f"{states_of_us[index]} - ", end='')
    print(dirty_dozen[random.randint(0, len(dirty_dozen) - 1)])


def main() -> None:
    parse = argparse.ArgumentParser()
    parse.add_argument('-o', '--option', type=int, choices=range(2),
                       default=0, help='selects function')
    args = parse.parse_args()

    if args.option == 0:
        func_1()
    if args.option == 1:
        func_2()


if __name__ == '__main__':
    main()
