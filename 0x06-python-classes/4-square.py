#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """Creating a square"""

    def __init__(self, size=0):
        """Initializing a new square object
            Args:
                size (int): The size of the new square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculating the area of the square"""

        result = self.__size ** 2
        return result

    @property
    def size(self):
        """a getter for the size variable"""

        return self.__size

    @size.setter
    def size(self, value):
        """a setter for the size variable"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
