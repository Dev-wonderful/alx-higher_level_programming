#!/usr/bin/python3
"""A module to define a base geometry"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """It validates a value
                Args:
                    name (str): The attribute that owns the value
                    value (int): to be validated
        """
