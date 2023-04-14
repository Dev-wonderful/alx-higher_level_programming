#!/usr/bin/python3
"""Defines a square class which inherits the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size):
        # Rectangle.__init__(self)
        """Initializes an Instance of a Square
                Args:
                    size (int): Must be a positive integer
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
