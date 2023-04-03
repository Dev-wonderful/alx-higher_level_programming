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

    def __str__(self):
        """Informal representation of the rectangle object"""
        s = []
        if self.__height and self.__width:
            for h in range(self.__height):
                for w in range(self.__width):
                    s.append("#")
                if h != (self.__height - 1):
                    s.append("\n")
            return "".join(s)
        else:
            print("")

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

    def area(self):
        """Calculate the area of a rectangle object"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of a rectangle object"""
        if self.__height and self.__width:
            return 2 * (self.__height + self.__width)
        else:
            return 0
