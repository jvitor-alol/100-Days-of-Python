#!/usr/bin/env python
import sys

from ascii_magic import AsciiArt
from termcolor import colored


def display_image(weeks_left: int) -> None:
    images_info = {
        'baby': {
            'url': 'https://tinyurl.com/2ef7bnye',
            'color': 'green'},
        'sunglasses': {
            'url': 'https://tinyurl.com/3fek42ym',
            'color': 'blue'},
        'skull': {
            'url': 'https://tinyurl.com/yu9edwtv',
            'color': 'red'},
    }

    if weeks_left <= 1404:  # Over 63
        url = images_info['skull']['url']
        color = images_info['skull']['color']
    elif weeks_left <= 3484:  # Over 23
        url = images_info['sunglasses']['url']
        color = images_info['sunglasses']['color']
    else:
        url = images_info['baby']['url']
        color = images_info['baby']['color']

    try:
        my_art = AsciiArt.from_url(url)
        my_art.to_terminal(columns=70)
    except OSError as e:
        print(f'Could not load the image, server said: {e.code} {e.msg}')

    print(colored(
        f"\n\t{"#" * 14} You have {weeks_left} weeks left {"#" * 14}"
        .upper(),
        color=color,
        attrs=['blink']))


def main() -> None:
    age = int(input("STATE YOUR AGE, MORTAL!\n"))

    if age == 69:
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')
        print(f"{age} \033[35m(nice)\033[0m")

    age_in_weeks = age * 52
    weeks_left = 4680 - age_in_weeks
    display_image(weeks_left)


if __name__ == '__main__':
    main()
