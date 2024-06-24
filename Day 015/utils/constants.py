"""
This module defines the constants used in the coffee machine application.

Constants:
    MENU (dict): A dictionary containing the menu items with their respective \
        ingredients and costs.
        'espresso': {
            'ingredients': {
                'water': 50,
                'coffee': 18,
            },
            'cost': 1.5,
        },
        'latte': {
            'ingredients': {
                'water': 200,
                'milk': 150,
                'coffee': 24,
            },
            'cost': 2.5,
        },
        'cappuccino': {
            'ingredients': {
                'water': 250,
                'milk': 100,
                'coffee': 24,
            },
            'cost': 3.0,
        }

    COINS (dict): A dictionary containing the coin types and their \
        respective values.
        'quarter': 0.25,
        'dime': 0.10,
        'nickle': 0.05,
        'penny': 0.01
"""

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

COINS = {
    'quarter': 0.25,
    'dime': 0.10,
    'nickle': 0.05,
    'penny': 0.01
}
