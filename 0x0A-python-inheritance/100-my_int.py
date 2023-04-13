#!/usr/bin/python3
"""Defines a class that inherits the int class"""


class MyInt(int):
    """A subclass of Int"""

    def __ne__(self, value):
        return self.real == value

    def __eq__(self, value):
        return self.real != value
