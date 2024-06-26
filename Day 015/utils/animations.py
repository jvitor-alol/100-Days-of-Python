"""
Module providing general purpose animations.

This module includes functions to display animated messages to the
user.

Functions:
    - three_dots_message(message, color_option, delay=0, clear=True):
        Displays a message followed by an animated three-dot ellipsis.
"""
import sys
import time

from termcolor import colored


def three_dots_message(
        message: str, color_option: str,
        delay: float = 0, clear: bool = True) -> None:
    """
    Display a message followed by an animated three-dot ellipsis.

    Args:
        message (str): The message to display before the animation.
        color_option (str): The color to use for the message and dots.
        delay (float, optional): The time to wait after the animation
            before clearing the line. Default is 0.
        clear (bool, optional): Whether to clear the line after the
            animation. Default is True.

    Returns:
        None
    """
    print(colored(message, color_option), end='', flush=True)
    time.sleep(0.5)
    for _ in range(3):
        print(colored(".", color_option), end='', flush=True)
        time.sleep(0.5)
    if clear:
        time.sleep(delay)
        sys.stdout.write('\033[2K\r')  # Clears line
