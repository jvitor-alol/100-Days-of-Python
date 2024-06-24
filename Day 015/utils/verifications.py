import sys
import time

from termcolor import colored

from typing import Callable


def check_input(message: str, condition: Callable[[str], bool],
                message_color: str = "white") -> str:
    """
    Prompts the user for input until a specified condition is met.

    Args:
        message (str): The message to display when prompting for user input.
        condition (Callable[[str], bool]): A function that takes the user's
            input as a string and returns a boolean indicating whether the
            condition is satisfied.
        message_color (str, optional): The color of the displayed message.
            Default is "white".

    Returns:
        str: The user's input that satisfies the specified condition.

    Exceptions:
        ValueError: Caught and logged if there is an error converting a value.
        Exception: Caught and logged if an unexpected error occurs.

    The loop will continue to prompt the user for input until the condition
    is satisfied. If an error occurs (ValueError or another Exception),
    a warning message will be logged and the input will be requested again.
    """

    def clear_input_line() -> None:
        sys.stdout.write('\033[F\033[K')
        print(colored("Insert a valid value", "red"), end='', flush=True)
        time.sleep(0.5)
        for _ in range(3):
            print(colored(".", "red"), end='', flush=True)
            time.sleep(0.5)
        sys.stdout.write('\033[2K\r')

    while True:
        value: str = input(colored(message, message_color))
        try:
            satisfies_condition: bool = condition(value)
        except ValueError:
            clear_input_line()
            # logger.warning(f"Error converting {value} to number: {ve}")
            continue
        # except Exception:
        #     clear_input_line()
        #     # logger.warning(f"Unexpected error: {e}")
        #     continue
        else:
            if satisfies_condition:
                return value
            else:
                clear_input_line()
