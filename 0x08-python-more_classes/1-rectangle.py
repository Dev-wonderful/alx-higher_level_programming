#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Defines a representation of rectangle a object."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle object
            Args:
                  width (int): The width of the rectangle
                  height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter: returns the width(__width)"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter: sets the width (__width)"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """getter: returns the height(__height)"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter: sets the height (__height)"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
