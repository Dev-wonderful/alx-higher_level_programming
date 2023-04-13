#!/usr/bin/python3

"""A module to append to a file or create and write if it doesn't exist"""


def append_write(filename="", text=""):
    """Append text to a file or create and write if it doesn't exist
        Args:
            filename (str): The name of the file
            text (str): The text to be appended to the end of the file
        Returns:
            int: the number of bytes written into the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
