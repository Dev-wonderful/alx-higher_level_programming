#!/usr/bin/python3

"""A module to serialize and save to a JSON file"""
json = __import__('json')


def save_to_json_file(my_obj, filename):
    """
    To serialize and save to JSON file
        Args:
            my_obj (obj): The object to be serialized
            filename (str): The name of the JSON file
    """
    with open(filename, 'a', encoding="utf-8") as j_file:
        json.dump(my_obj, j_file)
