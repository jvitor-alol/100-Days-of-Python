#!/usr/bin/env python
import random
import argparse

import my_module


def func_1() -> None:
    random_int = random.randint(1, 10)
    print(random_int)

    print(f"Pi = {my_module.PI}")

    random_number = random.randint(1, 100) * random.random()
    print(random_number)


def main() -> None:
    parse = argparse.ArgumentParser()
    parse.add_argument('-o', '--option', type=int, choices=range(2),
                       default=0, help='selects function')
    args = parse.parse_args()

    if args.option == 0:
        func_1()


if __name__ == '__main__':
    main()
