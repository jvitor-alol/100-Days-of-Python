#!/usr/bin/env python
import os

from utils import read_template_letter, get_invited_names, write_invitation

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIR = os.path.join(CURRENT_DIR, 'Output/ReadyToSend')
LETTER_PATH = os.path.join(CURRENT_DIR, 'Input/Letters/starting_letter.txt')
NAMES_FILEPATH = os.path.join(CURRENT_DIR, 'Input/Names/invited_names.txt')


def main() -> None:
    letter_content = read_template_letter(LETTER_PATH)
    names = get_invited_names(NAMES_FILEPATH)

    for name in names:
        write_invitation(letter_content, name, OUTPUT_DIR)


if __name__ == '__main__':
    main()
