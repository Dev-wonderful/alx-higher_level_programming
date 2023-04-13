#!/usr/bin/python3

"""A module to deserialize (convert JSON back to object)"""
json = __import__('json')


def from_json_string(my_str):
    """Deserializing
    Args:
        my_str (str): the string to be deserialized
    Returns:
         object: the original data
    """
    return json.loads(my_str)
