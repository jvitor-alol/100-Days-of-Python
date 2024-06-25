"""
Module representing a coffee machine with functionalities to make espresso, \
    latte, and cappuccino.

This module includes a Machine class that tracks resources such as water, \
    milk, coffee (in grams), and money, allows users to choose drinks, check \
    available resources, and refill resources as needed.
"""

import os
import sys

from .coffee import Coffee
from .verifications import check_input
from .constants import MENU, COINS


class CoffeeMachine:
    """
    Represents a coffee machine with functionalities to make espresso, latte, \
    and cappuccino.

    Attributes:
        - resources (dict): A dictionary tracking the current resources of \
            the coffee machine, including 'water' in milliliters, 'milk' in \
            milliliters, 'coffee' in grams, and 'money' in dollars.
        - espresso (Coffee): An instance of Coffee representing the espresso \
            drink with predefined ingredients and cost.
        - latte (Coffee): An instance of Coffee representing the latte drink \
            with predefined ingredients and cost.
        - cappuccino (Coffee): An instance of Coffee representing the \
            cappuccino drink with predefined ingredients and cost.
        - valid_options (tuple): A tuple containing valid menu options for \
            the coffee machine, including 'espresso', 'latte', 'cappuccino', \
            'off', 'report', and 'restock'.

    Methods:
        - display_menu() -> bool:
            Displays the menu options of the coffee machine, prompts the user \
            to choose a drink, and handles user interactions based on the \
            chosen option.

        - enough_ingredients(coffee_type: Coffee) -> bool:
            Checks if there are enough ingredients in the machine to make a \
            specific type of coffee.

        - make_coffee(coffee_type: Coffee, coffee_name: str) -> None:
            Processes the making of a specific type of coffee. Prompts the \
            user for coins, checks if enough money is inserted, and \
            dispenses change if needed.

        - machine_report() -> None:
            Prints a report of the current resources of the coffee machine.

        - machine_restock() -> None:
            Allows restocking of specific resources (water, milk, coffee) in \
            the coffee machine. Prompts the user for the type and amount of \
            resource to restock.
    """

    def __init__(self):
        """
        Initializes a new instance of the CoffeeMachine class with predefined \
            resources, coffee types and valid inputs.
        """
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'money': 0
        }

        self.espresso = Coffee(
            coffee=MENU['espresso']['ingredients']['coffee'],
            water=MENU['espresso']['ingredients']['water'],
            cost=MENU['espresso']['cost']
        )

        self.latte = Coffee(
            coffee=MENU['latte']['ingredients']['coffee'],
            milk=MENU['latte']['ingredients']['milk'],
            water=MENU['latte']['ingredients']['water'],
            cost=MENU['latte']['cost']
        )

        self.cappuccino = Coffee(
            coffee=MENU['cappuccino']['ingredients']['coffee'],
            milk=MENU['cappuccino']['ingredients']['milk'],
            water=MENU['cappuccino']['ingredients']['water'],
            cost=MENU['cappuccino']['cost']
        )

        self.valid_options = (
            'espresso', 'latte', 'cappuccino', 'off', 'report', 'restock')

    def display_menu(self) -> bool:
        """
        Displays the menu options of the coffee machine, prompts the user to \
            choose a drink, and handles user interactions based on the chosen \
            option.

        Returns:
            bool: True to continue running the machine, False to stop.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        option = check_input(
            "What would you like? (espresso/latte/cappuccino): ",
            lambda x: x.lower() in self.valid_options
        ).lower()

        match (option):
            case 'espresso':
                self.make_coffee(self.espresso, option)
            case 'latte':
                self.make_coffee(self.latte, option)
            case 'cappuccino':
                self.make_coffee(self.cappuccino, option)
            case 'off':
                print("Shutting off the machine")
                return False
            case 'report':
                self.machine_report()
            case 'restock':
                self.machine_restock()
            case _:
                print("Command not recognized")

        keep_on = check_input(  # Keeps the terminal from being cleared
            "Continue? [Y/n]: ",
            lambda x: x.lower() in ['y', 'n'] or x == '').lower()
        if keep_on == 'n':
            print("Shutting off the machine")
            return False

        return True

    def enough_ingredients(self, coffee_type: Coffee) -> bool:
        """
        Checks if there are enough ingredients in the machine to make a \
            specific type of coffee.

        Args:
            coffee_type (Coffee): An instance of Coffee representing the type \
                of coffee to be checked.

        Returns:
            bool: True if there are enough ingredients, False otherwise.
        """
        _missing_ingredients = []

        if coffee_type.coffee > self.resources['coffee']:
            _missing_ingredients.append('coffee')
        if coffee_type.water > self.resources['water']:
            _missing_ingredients.append('water')
        if coffee_type.milk > self.resources['milk']:
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

    def make_coffee(self, coffee_type: Coffee, coffee_name: str) -> None:
        """
        Processes the making of a specific type of coffee. Prompts the user \
            for coins, checks if enough money is inserted, and dispenses \
            change if needed.

        Args:
            coffee_type (Coffee): An instance of Coffee representing the type \
                of coffee to be made.
            coffee_name (str): The name of the coffee being made \
                (e.g., "espresso").

        Returns:
            None
        """
        if not self.enough_ingredients(coffee_type):
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
            self.resources['water'] -= coffee_type.water
            self.resources['milk'] -= coffee_type.milk
            self.resources['coffee'] -= coffee_type.coffee
            self.resources['money'] += coffee_type.cost

            if inserted_money > coffee_type.cost:
                change = round(inserted_money - coffee_type.cost, 2)
                print(f"Here is ${change} dollars in change.")

            print(f"Here is your {coffee_name}. Enjoy!")

    def machine_report(self) -> None:
        """
        Prints a report of the current resources of the coffee machine.

        Returns:
            None
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}")

    def machine_restock(self) -> None:
        """
        Allows restocking of specific resources (water, milk, coffee) in the \
        coffee machine. Prompts the user for the type and amount of resource \
        to restock.

        Returns:
            None
        """
        units = {'water': 'ml', 'milk': 'ml', 'coffee': 'g'}

        _ingredient = check_input(
            "Which ingredient are you restocking? ",
            lambda x: x.lower() in units.keys()
        ).lower()
        _amount = int(check_input(
            f"Insert the amount (in {units[_ingredient]}): ",
            lambda x: x.isdigit() and int(x) > 0
        ))

        self.resources[_ingredient] += _amount
        print(
            f"OK! Current {_ingredient} amount: {self.resources[_ingredient]}"
            f"{units[_ingredient]}.")

        restock_another = check_input(
            "Restock another item? [Y/n]: ",
            lambda x: x.lower() in ['y', 'n'] or x == '').lower()
        if restock_another == 'n':
            return
        # Clears 4 previous lines
        sys.stdout.write('\033[F\033[K')
        sys.stdout.write('\033[F\033[K')
        sys.stdout.write('\033[F\033[K')
        sys.stdout.write('\033[F\033[K')

        self.machine_restock()
