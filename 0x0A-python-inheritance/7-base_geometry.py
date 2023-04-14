#!/usr/bin/python3
"""A module to define a base geometry"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """It validates a value.
                Args:
                    name (str): The attribute that owns the value.
                    value (int): to be validated.
                Raises:
                    TypeError: if value is not an integer.
                    ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
