#!/usr/bin/python3

"""A module to read a file"""


def read_file(filename=""):
    """A function to read a file
        Args:
            filename (str): the name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
