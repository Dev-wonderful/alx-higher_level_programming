#!/usr/bin/python3
"""A Module for the Base Class"""


class Base:
    """A class to manage ID"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the instance.
            Args:
                  id (:obj: `int`, optional): Defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
