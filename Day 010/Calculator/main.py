#!/usr/bin/env python
import os
import sys

from termcolor import colored

from utils import LOGO
from utils import Calculator
from utils import is_number, check_input


def main() -> None:
    _keep_going = True
    _operations = {
        'addition': ['+', 'add', 'plus'],
        'subtraction': ['-', 'sub', 'subtract', 'minus'],
        'multiplication': ['x', '*', 'mult', 'multiply', 'times'],
        'division': ['/', 'div', 'divide']
    }
    valid_ops = _operations.values()

    while _keep_going:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(LOGO, "blue"))

        number_1 = is_number(check_input(
            "Insert first number: ", is_number))[0]
        operation = check_input(
            "Select an operation [ + | - | x | / ]: ",
            lambda x: any(x.lower() in symbols for symbols in valid_ops)) \
            .lower()
        number_2 = is_number(check_input(
            "Insert second number: ", is_number))[0]

        match(operation):
            case operation if operation in _operations['addition']:
                resultado = Calculator.addition(number_1, number_2)
                operator = '+'
            case operation if operation in _operations['subtraction']:
                resultado = Calculator.subtraction(number_1, number_2)
                operator = '-'
            case operation if operation in _operations['multiplication']:
                resultado = Calculator.multiplication(number_1, number_2)
                operator = 'x'
            case operation if operation in _operations['division']:
                try:
                    resultado = Calculator.division(number_1, number_2)
                except ZeroDivisionError as e:
                    print(colored("\n" + e.args[0], "green", attrs=["blink"]))
                    resultado = None
                operator = '/'
            case _:
                print("\nInvalid operation...")

        if resultado is not None:
            print(colored(
                f"\n{number_1} {operator} {number_2} = {resultado}",
                "green", attrs=["blink"]))

        again = check_input(
            "\nWould you like to calculate something else? [Y/n] ",
            lambda x: x.lower() in ['yes', 'y', 'no', 'n'] or x == '').lower()
        if again in ['n', 'no']:
            _keep_going = False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
