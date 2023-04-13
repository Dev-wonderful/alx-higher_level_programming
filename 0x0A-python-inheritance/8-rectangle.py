#!/usr/bin/python3
"""Defines a Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inheriting BaseGeometry"""

    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        """Initializing a Rectangle object
                Args:
                    width (int): the width of the object
                    height (int): the height of the object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
