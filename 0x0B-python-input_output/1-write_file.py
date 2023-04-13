#!/usr/bin/python3

"""A module to write into a file"""


def write_file(filename="", text=""):
    """A function to write a text to a file
        Args:
            filename (str): the name of the file
            text (str): The text to be written into the file
        Returns:
            int: the number of bytes written to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
