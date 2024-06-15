"""
This module defines a Calculator class to perform basic arithmetic operations.

The Calculator class includes methods for addition, subtraction,
multiplication, and division.
All methods are implemented as static methods since they do not
depend on the instance state of the Calculator class.

Usage example:
    calculator = Calculator()
    result_add = calculator.addition(3, 5.5)
    result_sub = calculator.subtract(10, 4)
    result_mul = calculator.multiplication(2, 3)
    result_div = calculator.division(10, 2)
"""

from typing import Union


class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    @staticmethod
    def addition(number_1: Union[int, float],
                 number_2: Union[int, float]) -> Union[int, float]:
        """
        Adds two numbers together.

        Args:
            number_1 (Union[int, float]): The first number.
            number_2 (Union[int, float]): The second number.

        Returns:
            Union[int, float]: The sum of the two numbers.
        """
        return number_1 + number_2

    @staticmethod
    def subtraction(number_1: Union[int, float],
                    number_2: Union[int, float]) -> Union[int, float]:
        """
        Subtracts the second number from the first number.

        Args:
            number_1 (Union[int, float]): The first number.
            number_2 (Union[int, float]): The second number.

        Returns:
            Union[int, float]: The result of the subtraction.
        """
        return number_1 - number_2

    @staticmethod
    def multiplication(number_1: Union[int, float],
                       number_2: Union[int, float]) -> Union[int, float]:
        """
        Multiplies two numbers together.

        Args:
            number_1 (Union[int, float]): The first number.
            number_2 (Union[int, float]): The second number.

        Returns:
            Union[int, float]: The product of the two numbers.
        """
        return number_1 * number_2

    @staticmethod
    def division(number_1: Union[int, float],
                 number_2: Union[int, float]) -> Union[int, float]:
        """
        Divides the first number by the second number.

        Args:
            number_1 (Union[int, float]): The first number.
            number_2 (Union[int, float]): The second number.

        Returns:
            Union[int, float]: The result of the division.

        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if number_2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return number_1 / number_2
