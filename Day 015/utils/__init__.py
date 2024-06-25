"""
This package provides utility modules and functions for the coffee machine \
application.

Modules:
    coffee: Defines the Coffee class used to represent different types of \
        coffee beverages.
    coffee_machine: Contains the CoffeeMachine class representing the \
        coffee machine itself.
    verifications: Provides utility functions for input validation.
    constants: Contains the menu and coin constants used in the application.

Imports:
    Coffee: Class representing a coffee beverage with its required \
        ingredients and cost.
    CoffeeMachine: Class representing the coffee machine with functionalities \
        to make espresso, latte, and cappuccino.
    check_input: Function to prompt the user for input until a specified \
        condition is met.
    MENU: Dictionary containing the menu items with their respective \
        ingredients and costs.
    COINS: Dictionary containing the coin types and their respective values.
"""

from .coffee import Coffee
from .coffee_machine import CoffeeMachine
from .verifications import check_input
from .constants import MENU, COINS

__all__ = ['Coffee', 'CoffeeMachine', 'check_input', 'MENU', 'COINS']