import os
import time
import sys
from textwrap import dedent
from typing import List

from .animations import *
from .verify import *

from ascii_magic import AsciiArt
from art import text2art
from termcolor import colored

IMAGES = {
    'level 1': './images/level_1.png',
    'level 2': './images/level_2.jpg',
    'level 3': './images/level_3.jpg',
    'game over': './images/game_over.png'
}


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


def render_level(image: str, message: str,
                 conditions: List, *additional_messages) -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    AsciiArt.from_image(image).to_terminal(columns=100)

    for text in additional_messages:
        print(colored(dedent(text), "green"))
        time.sleep(1)

    choice = check_input(
        message=message,
        conditions=conditions
    )

    return choice


def first_level() -> None:
    left_right = render_level(
        image=IMAGES['level 1'],
        message="\nYou're at a cross road. Do you go left or right? ",
        conditions=["left", "right", "l", "r"]
    )

    if left_right in ["l", "left"]:
        game_over("You fell into a hole".center(100))
    else:
        spinning_loader("You take the rightmost path", 3)
        second_level()


def second_level() -> None:
    swim_or_wait = render_level(
        IMAGES['level 2'],
        "Do you try to swim to the other side or wait for a boat? ",
        ["swim", "wait"],
        "\nYou've come to a lake. "
        "There is an island in the middle of the lake."
    )

    if swim_or_wait == "swim":
        game_over("You get attacked by an angry trout".center(100))
    else:
        spinning_loader("You've decided to wait for a boat", 3)
        final_level()


def final_level() -> None:
    door = render_level(
        IMAGES['level 3'],
        "One red, one yellow and one blue. Which colour do you choose? ",
        ["red", "yellow", "blue", "r", "y", "b"],
        "\nYou arrive at the island unharmed. There is a house with 3 doors."
    )

    if door in ["yellow", "y"]:
        win_screen()
    if door in ["red", "r"]:
        game_over("The room is catching fire".center(100))
    if door in ["blue", "b"]:
        game_over("It's a room full of beasts".center(100))


def win_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n\n\n\n\n\n\n")
    three_dots_message("\t\t\t\t\t\t", color_option=4)
    three_dots_message("\t\t\t\t\t\t", color_option=4)
    three_dots_message("\t\t\t\t\t\t", color_option=4)
    os.system('cls' if os.name == 'nt' else 'clear')

    message = colored("\t\t\tCONGRATULATIONS! YOU WON THE GAME!"
                      "\n\t\t\t\tHere's your prize!",
                      "blue", attrs=["blink"])
    for char in message:
        print(char, end="", flush=True)
        time.sleep(.1)

    time.sleep(.5)
    print("\n\n\n")
    treasure_chest = r"""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"'"-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
    """
    print(colored(treasure_chest, "yellow", attrs=["blink"]))


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
