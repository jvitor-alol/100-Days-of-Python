"""
This module defines the Coffee class used to represent different
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
        - name (str): The name of the coffee beverage.
        - cost (float): The cost of the coffee (in dollars).
        - water (int): The amount of water (in ml) needed to make the \
            coffee.
        - coffee (int): The amount of coffee (in grams) needed to make \
            the coffee.
        - milk (int): The amount of milk (in ml) needed to make the \
            coffee. Default is 0.

    Methods:
        - name (property): Gets the beverage name.
        - name.setter: Sets a name for the coffee. Must have four \
            characters at least.
        - cost (property): Gets the cost of the coffee in dollars.
        - cost.setter: Sets the cost of the coffee, must be a positive \
            value.
        - water (property): Gets the amount of water in ml.
        - water.setter: Sets the amount of water, must be a positive \
            value.
        - coffee (property): Gets the amount of coffee in grams.
        - coffee.setter: Sets the amount of coffee, must be a positive \
            value.
        - milk (property): Gets the amount of milk in ml.
        - milk.setter: Sets the amount of milk, must be a positive \
            value or zero.
    """

    def __init__(
            self, name: str, cost: float, water: int,
            coffee: int, milk: int = 0) -> None:
        """
        Constructs all the necessary attributes for the coffee object.

        Args:
            name (str): The name of the coffee beverage.
            cost (float): The cost of the coffee (in dollars).
            water (int): The amount of water (in ml) needed to make \
                the coffee.
            coffee (int): The amount of coffee (in grams) needed to \
                make the coffee.
            milk (int, optional): The amount of milk (in ml) needed to \
                make the coffee. Default is 0.
        """
        self._name = name
        self._cost = cost
        self._water = water
        self._coffee = coffee
        self._milk = milk

    @property
    def name(self) -> str:
        """Gets the beverage name."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Sets a name for the coffee. \
        Must have four characters at least.
        """
        if len(new_name) < 4:
            raise ValueError("Must have four characters at least")
        self._name = new_name

    @property
    def cost(self) -> float:
        """Gets the cost of the coffee in dollars."""
        return self._cost

    @cost.setter
    def cost(self, new_cost: float) -> None:
        """Sets the cost of the coffee. Must be a positive value."""
        if new_cost <= 0:
            raise ValueError("Must be a positive value")
        self._cost = new_cost

    @property
    def water(self) -> int:
        """Gets the amount of water in ml."""
        return self._water

    @water.setter
    def water(self, new_water: int) -> None:
        """Sets the amount of water. Must be a positive value."""
        if new_water <= 0:
            raise ValueError("Must be a positive value")
        self._water = new_water

    @property
    def coffee(self) -> int:
        """Gets the amount of coffee in grams."""
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee: int) -> None:
        """Sets the amount of coffee. Must be a positive value."""
        if new_coffee <= 0:
            raise ValueError("Must be a positive value")
        self._coffee = new_coffee

    @property
    def milk(self):
        """Gets the amount of milk in ml."""
        return self._milk

    @milk.setter
    def milk(self, new_milk: int) -> None:
        """Sets the amount of milk. Must be a positive value or zero."""
        if new_milk < 0:
            raise ValueError("Must be a positive value or zero")
        self._milk = new_milk
