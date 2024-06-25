#!/usr/bin/env python
import sys

from utils import CoffeeMachine, MENU


def main() -> None:
    is_on = True
    coffee_machine = CoffeeMachine(menu=MENU)
    # Initial resources
    coffee_machine.resources = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0
    }
    coffee_machine.options.extend([coffe_name for coffe_name in MENU.keys()])

    while is_on:
        is_on = coffee_machine.display()

    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
