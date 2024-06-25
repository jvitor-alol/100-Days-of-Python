import sys
import time

from termcolor import colored


def three_dots_message(
        message: str, color_option: str,
        delay: float = 0, clear: bool = True) -> None:
    print(colored(message, color_option), end='', flush=True)
    time.sleep(0.5)
    for _ in range(3):
        print(colored(".", color_option), end='', flush=True)
        time.sleep(0.5)
    time.sleep(delay)
    if clear:
        sys.stdout.write('\033[2K\r')  # Clears line
