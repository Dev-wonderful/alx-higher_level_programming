#!/usr/bin/python3
json = __import__('json')

"""A module to serialize a data (convert to JSON)"""


def to_json_string(my_obj):
    """Serilizing an obj
        Args:
            my_obj (object): the object to be serialized
        Returns:
            str: the serialized object
    """
    return json.dumps(my_obj)
