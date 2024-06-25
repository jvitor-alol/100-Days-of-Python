#!/usr/bin/env python
import sys

from utils import CoffeeMachine


def main() -> None:
    is_on = True
    coffee_machine = CoffeeMachine()

    while is_on:
        is_on = coffee_machine.display_menu()

    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
