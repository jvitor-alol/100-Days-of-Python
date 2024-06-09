#!/usr/bin/env python
import random


def main() -> None:
    chance = random.randint(0, 1)
    if chance:
        print("Heads")
    else:
        print("Tails")


if __name__ == '__main__':
    main()
