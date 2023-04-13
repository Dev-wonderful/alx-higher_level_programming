#!/usr/bin/python3
"""A module that creates a class which inherits from list"""


class MyList(list):
    """Inherits List class"""

    def print_sorted(self):
        """Prints the list in a sorted way but doesn't change the list"""

        item = self.copy()
        item.sort()
        print(item)
