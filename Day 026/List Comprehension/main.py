#!/usr/bin/env python
from argparse import ArgumentParser


def square_numbers() -> None:
    raise NotImplementedError


def filter_even_numbers() -> None:
    raise NotImplementedError


def data_overlap() -> None:
    raise NotImplementedError


def main() -> None:
    parse = ArgumentParser()
    parse.add_argument(
        "-o", "--option",
        type=int, choices=range(3), default=0,
        help="choose function")
    args = parse.parse_args()

    match args.option:
        case 0:
            square_numbers()
        case 1:
            filter_even_numbers()
        case 2:
            data_overlap()
        case _:
            print("Insert a valid option: {0, 1, 2}")


if __name__ == '__main__':
    main()
