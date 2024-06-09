#!/usr/bin/env python
from utils import *


def main() -> None:
    try:
        game_start()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
