"""
This module defines the constants used in the coffee machine \
application.

Constants:
    MENU (dict): A dictionary containing the menu items with their \
        respective ingredients and costs.
"""

from .coffee import Coffee

MENU = {
    'espresso': Coffee(
        name='Espresso',
        coffee=18,
        water=50,
        cost=1.5
    ),
    'latte': Coffee(
        name='Latte',
        coffee=24,
        milk=150,
        water=200,
        cost=2.5
    ),
    'cappuccino': Coffee(
        name='Cappuccino',
        coffee=24,
        milk=100,
        water=250,
        cost=3.0
    ),
    'mocha': Coffee(
        name='Mocha',
        coffee=20,
        milk=150,
        water=200,
        cost=3.5
    ),
    'americano': Coffee(
        name='Americano',
        coffee=18,
        water=300,
        cost=2.0
    ),
    'macchiato': Coffee(
        name='Macchiato',
        coffee=24,
        milk=50,
        water=100,
        cost=2.75
    )
}
