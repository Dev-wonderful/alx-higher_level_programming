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
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')

        if position[0] < 0 or position[1] < 0:
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

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
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

        if value[0] < 0 and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Printing the square based on size"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            if self.__position[1] >= 0:
                if self.__position[1] > 0:
                    for i in range(self.__position[0]):
                        print("_", end="")
                else:
                    for i in range(self.__position[0]):
                        print(" ", end="")

            for j in range(self.__size):
                print("#", end="" if j != (self.__size - 1) else "\n")
