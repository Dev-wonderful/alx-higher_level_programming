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
