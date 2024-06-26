"""
This package provides utility modules and functions for the coffee
machine application.

Modules:
    coffee: Defines the Coffee class used to represent different types
        of coffee beverages.
    coffee_machine: Contains the CoffeeMachine class representing the
        coffee machine itself.
    verifications: Provides utility functions for input validation.
    menu: Contains the coffee menu for the machine used in the
        application.
    animations: Provides functions for displaying animated messages.

Imports:
    Coffee: Class representing a coffee beverage with its required
        ingredients and cost.
    CoffeeMachine: Class representing the coffee machine with
        functionalities to make espresso, latte, and cappuccino.
    check_input: Function to prompt the user for input until a
        specified condition is met.
    three_dots_message: Function to display a message followed by an
        animated three-dot ellipsis.
    MENU: Dictionary containing the menu items with their respective
        ingredients and costs.
"""
from .coffee import Coffee
from .coffee_machine import CoffeeMachine
from .verifications import check_input
from .animations import three_dots_message
from .menu import MENU


__all__ = [
    'Coffee',
    'CoffeeMachine',
    'check_input',
    'three_dots_message',
    'MENU'
]
