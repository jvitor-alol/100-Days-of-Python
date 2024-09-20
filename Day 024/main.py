#!/usr/bin/env python
from os import getenv

from game_utils import game_loop


def main() -> None:
    game_loop(difficulty=getenv('DIFFICULTY', 'normal'))


if __name__ == '__main__':
    main()
