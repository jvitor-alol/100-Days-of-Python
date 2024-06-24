#!/usr/bin/env python
import os
import sys

from utils import Coffee
from utils import check_input
from utils import MENU, COINS

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
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


def make_coffee(coffee_type: Coffee, coffee_name: str) -> None:
    if not is_enough_ingredients(coffee_type):
        return

    print(f"-- Insert your coins (${coffee_type.cost:.2f}) --")
    quarters = int(check_input(
        "Quarters ($0.25): ",
        lambda x: x.isdigit()
    ))
    dimes = int(check_input(
        "Dimes ($0.10): ",
        lambda x: x.isdigit()
    ))
    nickles = int(check_input(
        "Nickles ($0.05): ",
        lambda x: x.isdigit()
    ))
    pennies = int(check_input(
        "Pennies ($0.01): ",
        lambda x: x.isdigit()
    ))

    inserted_money = (
        quarters * COINS['quarter'] +
        dimes * COINS['dime'] +
        nickles * COINS['nickle'] +
        pennies * COINS['penny']
    )

    if coffee_type.cost > inserted_money:
        print(
            f"Sorry that's not enough. Money refunded: ${inserted_money}.")
    else:
        RESOURCES['water'] -= coffee_type.water
        RESOURCES['milk'] -= coffee_type.milk
        RESOURCES['coffee'] -= coffee_type.coffee
        RESOURCES['money'] += coffee_type.cost

        if inserted_money > coffee_type.cost:
            change = round(inserted_money - coffee_type.cost, 2)
            print(f"Here is ${change:.2f} dollars in change.")

        print(f"Here is your {coffee_name}. Enjoy!")


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


def machine_report() -> None:
    print(f"Water: {RESOURCES['water']}ml")
    print(f"Milk: {RESOURCES['milk']}ml")
    print(f"Coffee: {RESOURCES['coffee']}g")
    print(f"Money: ${RESOURCES['money']}")


def display_menu(valid_options: tuple[str]) -> bool:
    os.system('cls' if os.name == 'nt' else 'clear')
    option = check_input(
        "What would you like? (espresso/latte/cappuccino): ",
        lambda x: x.lower() in valid_options
    ).lower()

    match (option):
        case 'espresso':
            make_coffee(ESPRESSO, option)
        case 'latte':
            make_coffee(LATTE, option)
        case 'cappuccino':
            make_coffee(CAPPUCCINO, option)
        case 'off':
            print("Shutting off the machine")
            return False
        case 'report':
            machine_report()
        case _:
            print("Command not recognized")

    keep_on = check_input(  # Keeps the terminal from being cleared
        "Continue? [Y/n]: ",
        lambda x: x.lower() in ['y', 'n'] or x == '').lower()
    if keep_on == 'n':
        return False

    return True


def main() -> None:
    is_on = True
    valid_options = ('espresso', 'latte', 'cappuccino', 'off', 'report')

    while is_on:
        is_on = display_menu(valid_options)

    sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
