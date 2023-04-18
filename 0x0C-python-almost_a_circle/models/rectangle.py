#!/usr/bin/python3
"""A modue to define a rectangle"""
from base import Base


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
