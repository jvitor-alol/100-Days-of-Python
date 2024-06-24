class Coffee:
    def __init__(self, water: int, coffee: int, cost: float, milk: int = 0):
        self._water = water
        self._coffee = coffee
        self._cost = cost
        self._milk = milk

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, new_water: int):
        if new_water <= 0:
            raise ValueError('Must be a positive value')
        self._water = new_water

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee: int):
        if new_coffee <= 0:
            raise ValueError('Must be a positive value')
        self._coffee = new_coffee

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost: float):
        if new_cost <= 0:
            raise ValueError('Must be a positive value')
        self._cost = new_cost

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, new_milk: int):
        if new_milk < 0:
            raise ValueError('Must be a positive value or zero')
        self._milk = new_milk
