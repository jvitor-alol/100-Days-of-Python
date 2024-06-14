#!/usr/bin/env python
import os
import re
import sys

from termcolor import colored

from check_input import check_input

LOGO = r"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""


def main() -> None:
    keep_running = 'yes'
    bidders = []

    while keep_running in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            colored("******* Welcome to the Secret Auction Program *******",
                    "green", attrs=["blink"]))
        print(LOGO)

        name = check_input(
            "What is your name? ",
            lambda s: bool(re.match(r'^[A-Za-z ]+$', s)))
        bid = int(check_input("What's your bid? $", lambda x: x.isdigit()))
        bidders.append({'name': name, 'bid': bid})

        keep_running = check_input(
            "Are there any other bidders? [y/n]: ",
            lambda x: x in ['yes', 'y', 'no', 'n']).lower()

    # Find highest bidder
    bidders.sort(key=lambda x: x['bid'], reverse=True)
    print(
        "\nThe winner is "
        f"{bidders[0]['name']} with a bid of ${bidders[0]['bid']}.")

    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
