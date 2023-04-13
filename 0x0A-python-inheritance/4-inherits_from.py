#!/usr/bin/python3

"""A module to check for same class"""


def inherits_from(obj, a_class):
    """checks for inheritance
        Args:
            obj: an object
            a_class: a type of class
        Returns:
            bool: True if obj is of type a_class, False otherwise
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
