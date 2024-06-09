#!/usr/bin/env python
import os
import time
import sys
from textwrap import dedent
from typing import List, Any

from termcolor import colored
from ascii_magic import AsciiArt
from art import text2art

IMAGES = {
    'level 1': './level_1.jpg',
    'level 2': './level_2.jpg',
    'level 3': './level_3.jpg',
    'game over': './game_over.png'
}


def spinning_loader(message: str, seconds: int, color_option: int = 2) -> None:
    sys.stdout.write("\033[?25l")  # Hide the cursor
    for _ in range(seconds):
        for symbol in ['\\', '|', '/', '-']:
            print(
                f"\033[3{color_option}m{message} {symbol}", end="", flush=True)
            time.sleep(0.25)
            sys.stdout.write('\033[2K\r')
    sys.stdout.write("\033[?25h")  # Show the cursor


def three_dots_message(message: str, color_option: int = 2) -> None:
    print(f"\033[3{color_option}m{message}", end='', flush=True)
    time.sleep(0.5)
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    else:
        sys.stdout.write('\033[2K\r')


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


def game_start() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored("********************* WELCOME TO *********************"
                  .center(100), "green", attrs=["blink"]))
    three_dots_message("\t\t\t\t\t\t")
    logo = r"""
                   _                                     _     _                 _ 
                  | |                                   (_)   | |               | |
                  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
                  | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
                  | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
                   \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
    """
    print(colored(logo, "green", attrs=["blink"]))
    print(colored("******** Your mission is to find the treasure ********\n\n"
                  .center(100), "green", attrs=["blink"]))

    time.sleep(1)
    keeps_playing = check_input(
        "\033[32mThis is a dangerous task."
        " Do you have what it takes to keep going? \033[0m",
        ["yes", "no", "y", "n"])

    if keeps_playing == "n" or keeps_playing == "no":
        print("\033[32mWise choice, matey!\033[0m")
        exit(1)
    spinning_loader("You have been warned", 3)
    first_level()


def first_level() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    AsciiArt.from_image(IMAGES['level 1']).to_terminal(columns=100)

    left_right = check_input(
        "\nYou're at a cross road. Do you go left or right? ",
        ["left", "right", "l", "r"]
    )

    if left_right in ["l", "left"]:
        game_over("You fell into a hole".center(100))
    else:
        spinning_loader("You chose the rightmost path", 3)
        second_level()


def second_level() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    AsciiArt.from_image(IMAGES['level 2']).to_terminal(columns=100)

    print(colored(
        "\nYou've come to a lake. There is an island in the middle of the lake.",
        "green"))
    time.sleep(1)
    swim_or_wait = check_input(
        "Do you try to swim to the other side or wait for a boat? ",
        ["swim", "wait"]
    )

    if swim_or_wait == "swim":
        game_over("You get attacked by an angry trout.".center(100))
    else:
        spinning_loader("You've decided to wait for a boat", 3)
        final_level()


def final_level() -> None:
    pass


def game_over(reason: str) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    art = AsciiArt.from_image(IMAGES['game over'])
    art_string = art.to_ascii(columns=50)

    # art margin
    lines = art_string.splitlines()
    prefixed_lines = ["\t\t\t" + line for line in lines]
    art_string = '\n'.join(prefixed_lines)
    print(art_string)

    three_dots_message(f"{reason}\n\t\t\t\t\t\t", color_option=1)
    print(colored(text2art("YOU ARE DEAD", font="poison"), "red"))
    exit(1)


def main() -> None:
    try:
        game_start()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
