#!/usr/bin/python3
"""A module that creates a class which inherits from list"""


class MyList(list):
    """Inherits List class"""

    iterable = []

    def __init__(self, *args):
        """Initialize the derived class"""
        super().__init__(self, *args)
	self.iterable = args

    def print_sorted(self):
        """Prints the list in a sorted way but doesn't change the list"""

        item = self.copy(self.iterable)
        sort = self.sort()
        return item.sort()
