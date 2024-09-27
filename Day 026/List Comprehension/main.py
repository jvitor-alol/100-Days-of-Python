#!/usr/bin/env python
from os.path import join, dirname, abspath
from argparse import ArgumentParser

FILE_1_TXT = join(dirname(abspath(__file__)), 'file1.txt')
FILE_2_TXT = join(dirname(abspath(__file__)), 'file2.txt')


def square_numbers(numbers: list[int]) -> None:
    squared_numbers = [n ** 2 for n in numbers]
    print(squared_numbers)


def filter_even_numbers(list_of_strings: list[str]) -> None:
    numbers = [int(n) for n in list_of_strings]
    result = [n for n in numbers if n % 2 == 0]
    print(result)

    # one-liner
    # result = list(filter(lambda n: n % 2 == 0, map(int, list_of_strings)))
    # print(result)


def data_overlap() -> None:
    with open(FILE_1_TXT) as file1, open(FILE_2_TXT) as file2:
        a_list = list(map(int, file1.readlines()))
        b_list = list(map(int, file2.readlines()))

    result = [num for num in a_list if num in b_list]

    print(result)


def main() -> None:
    parse = ArgumentParser()
    parse.add_argument(
        "-o", "--option",
        type=int, choices=range(3), default=0,
        help="choose function")
    args = parse.parse_args()

    match args.option:
        case 0:
            square_numbers([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        case 1:
            filter_even_numbers(
                ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99'])
        case 2:
            data_overlap()
        case _:
            print("Insert a valid option: {0, 1, 2}")


if __name__ == '__main__':
    main()
