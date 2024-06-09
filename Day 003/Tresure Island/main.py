#!/usr/bin/env python
import sys

import utils


def main() -> None:
    try:
        utils.game_start()
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
