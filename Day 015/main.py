#!/usr/bin/env python
import os
import sys

from utils import MENU, COINS
from utils import check_input
from utils import Coffee

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ESPRESSO = Coffee(
    coffee=MENU['espresso']['ingredients']['coffee'],
    water=MENU['espresso']['ingredients']['water'],
    cost=MENU['espresso']['cost']
)

LATTE = Coffee(
    coffee=MENU['latte']['ingredients']['coffee'],
    milk=MENU['latte']['ingredients']['milk'],
    water=MENU['latte']['ingredients']['water'],
    cost=MENU['latte']['cost']
)

CAPPUCCINO = Coffee(
    coffee=MENU['cappuccino']['ingredients']['coffee'],
    milk=MENU['cappuccino']['ingredients']['milk'],
    water=MENU['cappuccino']['ingredients']['water'],
    cost=MENU['cappuccino']['cost']
)


def make_coffee(coffee_type: Coffee) -> None:
    if is_enough_ingredients(coffee_type):
        print("-- Insert your coins --")
        quarters = check_input(
            "Quarters: ",
            lambda x: int(x).isdigit()
        )
        dimes = check_input(
            "Dimes: ",
            lambda x: int(x).isdigit()
        )
        nickles = check_input(
            "Nickles: ",
            lambda x: int(x).isdigit()
        )
        pennies = check_input(
            "Pennies: ",
            lambda x: int(x).isdigit()
        )

    total_money = (
        quarters * COINS['quarter'] +
        dimes * COINS['dime'] +
        nickles * COINS['nickle'] +
        pennies * COINS['penny']
    )

    if coffee_type.cost > total_money:
        print(
            f"Sorry that's not enough money. Money refunded: $ {total_money}.")


def is_enough_ingredients(coffee_type: Coffee) -> bool:
    _missing_ingredients = []

    if coffee_type.coffee > RESOURCES['coffee']:
        _missing_ingredients.append('coffee')
    if coffee_type.water > RESOURCES['water']:
        _missing_ingredients.append('water')
    if coffee_type.milk > RESOURCES['milk']:
        _missing_ingredients.append('milk')

    if _missing_ingredients:
        if len(_missing_ingredients) == 1:
            message = f"{_missing_ingredients[0]}."
        else:
            message = (
                f"{', '.join(_missing_ingredients[:-1])} "
                f"or {_missing_ingredients[-1]}.")

        print(f"Sorry there is not enough {message}")
        return False
    else:
        return True


def machine_report():
    pass


def display_menu(valid_options: tuple[str]) -> bool:
    os.system('cls' if os.name == 'nt' else 'clear')
    option = check_input(
        "What would you like? (espresso/latte/cappuccino): ",
        lambda x: x.lower() in valid_options
    ).lower()

    match (option):
        case 'espresso':
            make_coffee(ESPRESSO)
        case 'latte':
            make_coffee(LATTE)
        case 'cappuccino':
            make_coffee(CAPPUCCINO)
        case 'off':
            print("Shutting off the machine")
            return False
        case 'report':
            machine_report()
        case _:
            print("Command not recognized")

    return True


def main() -> None:
    is_on = True
    valid_options = ('espresso', 'latte', 'cappuccino', 'off', 'report')

    while is_on:
        is_on = display_menu(valid_options)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
