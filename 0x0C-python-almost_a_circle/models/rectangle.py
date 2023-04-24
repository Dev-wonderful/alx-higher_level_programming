#!/usr/bin/python3
"""A module to define a rectangle"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle Class"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initializing a rectangle object
            Args:
                width: the width of the rectangle
                height: the height of the rectangle
                x (:obj: `int`, optional): x coordinate for printing
                y (:obj: `int`, optional): y coordinate for printing
                id (:obj: `int`, optional): A super class attribute
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @width.setter
    def width(self, value: int):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value: int):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value: int):
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value: int):
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for vertical_space in range(self.__y):
            print()
        for height in range(self.__height):
            hor = [" "] * self.__x
            width = ["#"] * self.__width
            hor += width
            for value in hor:
                print("{}".format(value), end="")
            print()
