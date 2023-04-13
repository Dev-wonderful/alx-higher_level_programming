#!/usr/bin/python3

"""A module to check for same class"""


def is_same_class(obj, a_class):
    """checks for inheritance
        Args:
            obj: an object
            a_class: a type of class
        Returns:
            bool: True if obj is of type a_class, False otherwise
    """
    return type(obj) is a_class
