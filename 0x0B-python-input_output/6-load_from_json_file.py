#!/usr/bin/python3

"""A module to load data from a JSON file"""
json = __import__('json')


def load_from_json_file(filename):
    """
    deserialize the JSON file
        Args:
            filename (str): The name of the file
    """
    with open(filename, 'r', encoding="utf-8") as j_file:
        return json.load(j_file)
