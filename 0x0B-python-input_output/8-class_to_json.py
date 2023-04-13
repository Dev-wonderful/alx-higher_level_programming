#!/usr/bin/python3

"""A module to convert class attributes to JSON"""


def class_to_json(obj):
    """Converts an object's attribute to a dictionary
        Args:
            obj (object): The instance of a class
        Returns:
            dict: A dictionary mapping all attributes to their values
    """
    return vars(obj)