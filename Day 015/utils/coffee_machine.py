"""
Module representing a coffee machine with functionalities to make
different types of coffee.

This module includes the CoffeeMachine class that tracks resources
such as water, milk, coffee (in grams), and money, allows users to
choose drinks, check available resources, and refill resources as
needed.

Classes:
    CoffeeMachine: Represents a coffee machine with predefined \
    resources and menu options.

Constants:
    LOGO (str): ASCII art logo for the coffee machine.
    UNITS (dict): Units for resources (water, milk, coffee, money).
    COINS (dict): Coin values in dollars.
    DEFAULT_MENU (dict): Default menu with predefined coffee types.
"""
import os
from typing import Union
from textwrap import dedent

from prettytable import PrettyTable
from termcolor import colored
from art import text2art

from .coffee import Coffee
from .verifications import check_input
from .animations import three_dots_message

LOGO = colored(text2art("COFFEE MACHINE", font='tarty1'), "green")
UNITS = {'water': 'ml', 'milk': 'ml', 'coffee': 'g', 'money': '$'}
COINS = {
    'quarter': 0.25,
    'dime': 0.10,
    'nickle': 0.05,
    'penny': 0.01
}
DEFAULT_MENU = {
    'espresso': Coffee(
        name='Espresso',
        coffee=18,
        water=50,
        cost=1.5
    )
}


class CoffeeMachine:
    """
    A class representing a coffee machine with predefined resources \
    and menu options.

    Attributes:
        - menu (dict): A dictionary containing the coffee types
            available in the machine.
        - options (list): A list of valid options for the machine
            (default options: 'off', 'report', 'restock').
        - resources (dict): A dictionary tracking the machine's
            resources, including water, milk, coffee, and money.

    Methods:
        - resources (property): Gets the current resources of the
            machine.
        - resources.setter: Sets the resources for the machine. All
            resources must be set and non-negative.
        - menu (property): Gets the coffee menu of the machine.
        - menu.setter: Sets a new menu. Must contain at least one type
            of coffee.
        - options (property): Gets the valid options for the machine.
        - options.setter: Sets new valid options. Must include the
            default operations.
        - display(): Displays the menu options, prompts user
            interaction, and handles chosen options. Returns True to
            continue, False to stop.
        - is_ingredients_sufficient(coffee_type): Checks if there are
            enough ingredients for the specified coffee type. Returns
            True if sufficient, False otherwise.
        - insert_coins(): Static method that processes inserted coins
            and returns the total amount in dollars.
        - make_coffee(coffee_type): Processes the making of the
            specified coffee type. Handles ingredient checks, coin
            insertion, and dispenses change if needed.
        - machine_report(): Prints a report of the current resources.
        - machine_restock(): Allows restocking of specific resources.
            Prompts the user for the type and amount of resource to
            restock.
    """

    def __init__(self, menu: dict[str, Coffee] = DEFAULT_MENU) -> None:
        """
        Initialize a new instance of the CoffeeMachine class.

        Args:
            menu (dict): A dictionary of coffee types available in the
                machine.
        """
        self._menu = menu
        self._options = ['off', 'report', 'restock']
        self._resources = {
            'water': 0,
            'milk': 0,
            'coffee': 0,
            'money': 0.0
        }

    @property
    def resources(self) -> dict[str, Union[int, float]]:
        """
        Get current coffee machine resources.

        Returns:
            dict: A dictionary of current resources.
        """
        return self._resources

    @resources.setter
    def resources(self, new_resources: dict[str, Union[int, float]]) -> None:
        """
        Set the resources for a coffee machine instance.

        Args:
            new_resources (dict): A dictionary with new resources.

        Raises:
            ValueError: If any resource is missing or negative.
        """
        if (('water' not in new_resources.keys()) or
            ('milk' not in new_resources.keys()) or
            ('coffee' not in new_resources.keys()) or
                ('money' not in new_resources.keys())):
            raise ValueError("All resources must be set")

        for key, value in new_resources.items():
            if key not in ['water', 'milk', 'coffee', 'money']:
                raise ValueError("Invalid resource key")
            if value < 0:
                raise ValueError(f"Resource '{key}' must be at least 0")

        self._resources = new_resources

    @property
    def menu(self) -> dict[str, Coffee]:
        """
        Get coffee machine menu.

        Returns:
            dict: A dictionary of coffee types available in the
            machine.
        """
        return self._menu

    @menu.setter
    def menu(self, new_menu: dict[str, Coffee]) -> None:
        """
        Set a menu.

        Args:
            new_menu (dict): A dictionary with new menu items.

        Raises:
            ValueError: If the menu is empty or invalid.
        """
        if not new_menu:
            raise ValueError("Menu must contain at least one item")

        for k, v in new_menu.items():
            if not isinstance(k, str) or not isinstance(v, Coffee):
                raise ValueError(dedent(
                    """Invalid item in the menu: \
                    key = {} | value = {}
                    """).format(type(k), type(v)))
        self._menu = new_menu

    @property
    def options(self) -> list[str]:
        """
        Get all valid options for the machine.

        Returns:
            list: A list of valid options.
        """
        return self._options

    @options.setter
    def options(self, new_options: list[str]) -> None:
        """
        Set all valid options.

        Args:
            new_options (list): A list with new options.

        Raises:
            ValueError: If required options are missing.
        """
        if (('off' not in new_options) or ('restock' not in new_options) or
                ('report' not in new_options)):
            raise ValueError("Options must contain all default operations")
        self._options = new_options

    def display(self) -> bool:
        """
        Display the menu options of the coffee machine.

        Prompts the user to choose a drink and handles user
        interactions.

        Returns:
            bool: True to continue running the machine, False to stop.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_table = PrettyTable()
        menu_table.field_names = ['Coffee', 'Price']
        menu_table.add_rows([
            [coffee_type.name, f"$ {coffee_type.cost:.2f}"] for
            coffee_type in self.menu.values()
        ])
        menu_table.align = 'l'
        print(LOGO + '\n\n')
        # Display centered rainbow menu_table
        for i, line in enumerate(str(menu_table).split('\n')):
            print(f"\033[3{i % 6 + 1}m\t\t\t\t\t" + line)

        coffee_selection = ', '.join(list(self.menu.keys())[:3]) + '...'
        print('\n')
        option = check_input(
            "\033[1;32;40mWhat would you like? "
            f"({coffee_selection}): \033[1;35;40m",
            lambda x: x.lower() in self.options
        ).lower()

        match (option):
            case 'off':
                three_dots_message("Shutting off the machine", "green")
                print(colored("Goodbye", "green"))
                return False
            case 'report':
                self.machine_report()
            case 'restock':
                self.machine_restock()
            case _:
                self.make_coffee(self.menu[option])
        return True

    def is_ingredients_sufficient(self, coffee_type: Coffee) -> bool:
        """
        Check if there are enough ingredients to make a specific coffee.

        Args:
            coffee_type (Coffee): The type of coffee to be checked.

        Returns:
            bool: True if there are enough ingredients, False otherwise.
        """
        missing_ingredients = []

        if coffee_type.coffee > self.resources['coffee']:
            missing_ingredients.append('coffee')
        if coffee_type.water > self.resources['water']:
            missing_ingredients.append('water')
        if coffee_type.milk > self.resources['milk']:
            missing_ingredients.append('milk')

        if missing_ingredients:
            if len(missing_ingredients) == 1:
                ingredients_str = f"{missing_ingredients[0]}"
            else:
                ingredients_str = (
                    f"{', '.join(missing_ingredients[:-1])} "
                    f"or {missing_ingredients[-1]}")

            three_dots_message(
                "Sorry, there is not enough {} for a {}".format(
                    ingredients_str, coffee_type.name.lower()),
                "green",
                delay=1.5)
            return False
        else:
            return True

    @staticmethod
    def insert_coins() -> float:
        """
        Process the number of coins inserted and return the total.

        Returns:
            float: The sum in dollars of all inserted coins.
        """
        num_quarters = int(check_input(
            "\t\033[1;32;40m    - Quarters ($0.25): \033[1;35;40m",
            lambda x: x.isdigit()
        ))
        num_dimes = int(check_input(
            "\t\033[1;32;40m    - Dimes ($0.10): \033[1;35;40m",
            lambda x: x.isdigit()
        ))
        num_nickles = int(check_input(
            "\t\033[1;32;40m    - Nickles ($0.05): \033[1;35;40m",
            lambda x: x.isdigit()
        ))
        num_pennies = int(check_input(
            "\t\033[1;32;40m    - Pennies ($0.01): \033[1;35;40m",
            lambda x: x.isdigit()
        ))

        total_money = (
            num_quarters * COINS['quarter'] +
            num_dimes * COINS['dime'] +
            num_nickles * COINS['nickle'] +
            num_pennies * COINS['penny']
        )
        return total_money

    def make_coffee(self, coffee_type: Coffee) -> None:
        """
        Process the making of a specific type of coffee.

        Prompts the user for coins, checks if enough money is inserted,
        and dispenses change if needed.

        Args:
            coffee_type (Coffee): The type of coffee to be made.
        """
        if not self.is_ingredients_sufficient(coffee_type):
            return

        print(colored(
            f"\n\t**** Insert your coins (${coffee_type.cost:.2f}) ****\n",
            "green"))
        inserted_money = self.insert_coins()

        message = "\n"

        if coffee_type.cost > inserted_money:
            message += "Sorry that's not enough 😣. Money refunded: ${:.2f}" \
                .format(inserted_money)
        else:
            self.resources['water'] -= coffee_type.water
            self.resources['milk'] -= coffee_type.milk
            self.resources['coffee'] -= coffee_type.coffee
            self.resources['money'] += coffee_type.cost

            if inserted_money > coffee_type.cost:
                change = round(inserted_money - coffee_type.cost, 2)
                message += f"Here is ${change} dollars in change. "
            message += f"Enjoy your {coffee_type.name.lower()} ☕!"

        print(colored(message, "blue"))
        three_dots_message("Press any key to continue", "blue", clear=False)
        input()

    def machine_report(self) -> None:
        """
        Print a report of the current resources of the coffee machine.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("*********** REPORT ***********\n", "red"))
        for k, v in self.resources.items():
            if k == 'money':
                print(f"- {k.title()}: {UNITS[k]}{v:.2f}")
                continue
            print(f"- {k.title()}: {v}{UNITS[k]}")
        input(colored("\nPress any key to continue...", "green"))

    def machine_restock(self) -> None:
        """
        Allow restocking of specific resources in the coffee machine.

        Prompts the user for the type and amount of resource to
        restock.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("**************** RESTOCK ****************\n", "red"))

        options = list(filter(lambda x: x != 'money', self.resources.keys()))
        ingredient = check_input(
            "\033[1;32;40mWhich item are you restocking? [{}]: \033[1;35;40m"
            .format('/'.join(options)),
            lambda x: x in options
        ).lower()
        amount = int(check_input(
            "\033[1;32;40mInsert the amount in {}: \033[1;35;40m"
            .format(UNITS[ingredient]),
            lambda x: x.isdigit() and int(x) > 0
        ))

        self.resources[ingredient] += amount
        confirm_message = "DONE! Current {} amount: {}{}.".format(
            ingredient, self.resources[ingredient], UNITS[ingredient])
        print(colored(confirm_message + '\n', "green"))

        restock_another = check_input(
            "\033[1;32;40mRestock another item? [y/N]: \033[1;35;40m",
            lambda x: x.lower() in ['y', 'n'] or x == '').lower()
        if restock_another != 'y':
            return
        self.machine_restock()
