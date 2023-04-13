#!/usr/bin/python3

"""A module that defines a student class"""


class Student:
    """A class template for students"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of a class
                Args:
                    first_name (str): The firstname of the student
                    last_name (str): The lastname of a student
                    age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the fields and its data to a dictionary
                Args:
                    self (obj): the instance of this class
                Returns:
                    dict: a dictionary containing the field and its data
        """
        return vars(self)
