import time
import sys
import re
from typing import Callable, Any

from termcolor import colored


def three_dots_message(message: str, color_option: str) -> None:
    print(colored(message, color_option), end='', flush=True)
    time.sleep(0.5)
    for _ in range(3):
        print(colored(".", color_option), end='', flush=True)
        time.sleep(0.5)
    sys.stdout.write('\033[2K\r')  # Clears line


def spinning_loader(message: str, seconds: int,
                    color_option: str = "white") -> None:
    sys.stdout.write("\033[?25l")  # Hide the cursor
    for _ in range(seconds):
        for symbol in ['\\', '|', '/', '-']:
            print(
                colored(f"{message} {symbol}", color_option),
                end="",
                flush=True)
            time.sleep(0.25)
            sys.stdout.write('\033[2K\r')
    sys.stdout.write("\033[?25h")  # Show the cursor


def is_single_letter(value: str) -> bool:
    if re.match("^[a-zA-Z]$", value):
        return True
    else:
        return False


def check_input(message: str, condition: Callable[[str], bool],
                message_color: str = "white") -> Any:
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
        Any: The user's input that satisfies the specified condition.

    Exceptions:
        ValueError: Caught and logged if there is an error converting a value.
        Exception: Caught and logged if an unexpected error occurs.

    The loop will continue to prompt the user for input until the condition
    is satisfied. If an error occurs (ValueError or another Exception),
    a warning message will be logged and the input will be requested again.
    """

    def clear_input_line():
        sys.stdout.write('\033[F\033[K')
        three_dots_message("Insert a valid value", "red")

    while True:
        value: str = input(colored(message, message_color))
        try:
            satisfies_condition: bool = condition(value)
        except ValueError as ve:
            clear_input_line()
            print(f"Error converting {value} to number: {ve}")
            # logger.warning(f"Error converting {value} to number: {ve}")
            continue
        except Exception as e:
            clear_input_line()
            print(f"Unexpected error: {e}")
            # logger.warning(f"Unexpected error: {e}")
            continue
        else:
            if satisfies_condition:
                return value
            else:
                clear_input_line()
