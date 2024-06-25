#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser

from turtle import Turtle, Screen
from prettytable import PrettyTable, from_csv


def table_test() -> None:
    table_1 = PrettyTable()
    table_1.field_names = [
        "City name", "Area", "Population", "Annual Rainfall"]
    table_1.add_rows(
        [
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4],
            ["Darwin", 112, 120900, 1714.7],
            ["Hobart", 1357, 205556, 619.5],
            ["Sydney", 2058, 4336374, 1214.8],
            ["Melbourne", 1566, 3806092, 646.9],
            ["Perth", 5386, 1554769, 869.4],
        ]
    )
    table_1.align = 'l'
    print(table_1)

    # read pokémon csv running from any directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'table.csv')

    with open(csv_path, mode='r', encoding='utf-8') as file:
        table_2 = from_csv(file)
    print(table_2)


def turtle_test() -> None:
    my_screen = Screen()
    twinkle_toes = Turtle(shape='turtle')
    twinkle_toes.color('LightGoldenrod', 'DeepSkyBlue2')

    # drawing a triangle
    twinkle_toes.forward(100)
    twinkle_toes.left(120)
    twinkle_toes.forward(100)
    twinkle_toes.left(120)
    twinkle_toes.forward(100)

    # print(my_screen.canvheight)
    my_screen.exitonclick()


def main() -> None:
    parse = ArgumentParser()
    parse.add_argument('-m', '--mode', type=int,
                       choices=range(2), required=True)
    args = parse.parse_args()

    match (args.mode):
        case 0:
            table_test()
        case 1:
            turtle_test()
        case _:
            sys.exit(1)


if __name__ == '__main__':
    main()
