import sys
from typing import List, Any

from termcolor import colored

from .animations import three_dots_message


def clear_previous_line() -> None:
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')


def check_input(message: str, conditions: List) -> Any:
    while True:
        value = input(colored(message, "green")).lower()
        if value not in conditions:
            clear_previous_line()
            three_dots_message("Insert a valid value", color_option=1)
        else:
            return value
