"""
This module defines the Coffee class used to represent different \
    types of coffee beverages.

Classes:
    Coffee: Represents a coffee beverage with its required \
        ingredients and cost.
"""


class Coffee:
    """
    A class representing a coffee beverage with its
    required ingredients and cost.

    Attributes:
        water (int): The amount of water (in ml) needed to make the coffee.
        coffee (int): The amount of coffee (in grams) needed to make \
            the coffee.
        cost (float): The cost of the coffee (in dollars).
        milk (int): The amount of milk (in ml) needed to make the coffee. \
            Default is 0.

    Methods:
        water (property): Gets the amount of water.
        water.setter: Sets the amount of water, must be a positive value.
        coffee (property): Gets the amount of coffee.
        coffee.setter: Sets the amount of coffee, must be a positive value.
        cost (property): Gets the cost of the coffee.
        cost.setter: Sets the cost of the coffee, must be a positive value.
        milk (property): Gets the amount of milk.
        milk.setter: Sets the amount of milk, must be a positive value or zero.
    """

    def __init__(self, water: int, coffee: int, cost: float, milk: int = 0):
        """
        Constructs all the necessary attributes for the coffee object.

        Args:
            water (int): The amount of water (in ml) needed to make the coffee.
            coffee (int): The amount of coffee (in grams) needed to \
                make the coffee.
            cost (float): The cost of the coffee (in dollars).
            milk (int, optional): The amount of milk (in ml) needed to \
                make the coffee. Default is 0.
        """
        self._water = water
        self._coffee = coffee
        self._cost = cost
        self._milk = milk

    @property
    def water(self):
        """Gets the amount of water."""
        return self._water

    @water.setter
    def water(self, new_water: int):
        """Sets the amount of water. Must be a positive value."""
        if new_water <= 0:
            raise ValueError('Must be a positive value')
        self._water = new_water

    @property
    def coffee(self):
        """Gets the amount of coffee."""
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee: int):
        """Sets the amount of coffee. Must be a positive value."""
        if new_coffee <= 0:
            raise ValueError('Must be a positive value')
        self._coffee = new_coffee

    @property
    def cost(self):
        """Gets the cost of the coffee."""
        return self._cost

    @cost.setter
    def cost(self, new_cost: float):
        """Sets the cost of the coffee. Must be a positive value."""
        if new_cost <= 0:
            raise ValueError('Must be a positive value')
        self._cost = new_cost

    @property
    def milk(self):
        """Gets the amount of milk."""
        return self._milk

    @milk.setter
    def milk(self, new_milk: int):
        """Sets the amount of milk. Must be a positive value or zero."""
        if new_milk < 0:
            raise ValueError('Must be a positive value or zero')
        self._milk = new_milk
