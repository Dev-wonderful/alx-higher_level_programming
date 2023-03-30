#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """Creating a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square object
            Args:
                size (int): The size of the new square
                position (tuple): The offset of the square printing
        """

        self.__raise_exception_size(size)
        self.__raise_exception_pos(position)
        self.__size = size
        self.__position = position

    @staticmethod
    def __raise_exception_size(value):
        """To handle exceptions for __size variable"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    @staticmethod
    def __raise_exception_pos(value):
        """To handle exceptions for __position variable"""

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

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
        """a setter for the size variable
            Args:
                value (int): assigned to __size variable
        """

        self.__raise_exception_size(value)
        self.__size = value

    @property
    def position(self):
        """A getter for the position variable"""

        return self.__position

    @position.setter
    def position(self, value):
        """A setter for the position variable
            Args:
                value (tuple): to be assigned to __position  variable
        """

        self.__raise_exception_pos(value)
        self.__position = value

    def my_print(self):
        """Printing the square based on size and position (x, y) axis"""

        if self.__size == 0:
            print()

        # horizontal indentation
        if self.__position[1] > 0 and self.__size > 0:
            for pos_y in range(self.__position[1]):
                print()

        for i in range(self.__size):
            if self.__position[0] > 0:  # vertical indentation
                for pos_x in range(self.__position[0]):
                    print(" ", end="")

            for j in range(self.__size):
                print("#", end="" if j != (self.__size - 1) else "\n")
