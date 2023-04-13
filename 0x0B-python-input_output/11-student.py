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

    def to_json(self, attr=None):
        """Converts the fields and its data to a dictionary
                Args:
                    self (obj): the instance of this class
                    attr (list): Optional filter with list of keys
                Returns:
                    dict: a dictionary containing the field and its data
        """
        if attr is None:
            return vars(self)
        else:
            my_dict = {}
            attr_dict = vars(self)
            for key in attr:
                # if attr == 'first_name':
                #     my_dict['firstname'] = self.first_name
                # elif attr == 'last_name':
                #     my_dict['last_name'] = self.last_name
                # elif attr == 'age':
                #     my_dict['age'] = self.age
                if key in attr_dict:
                    my_dict[key] = attr_dict[key]

            return my_dict

    def reload_from_json(self, json):
        """reload attributes of an instance using a dictionary
                Args:
                    json (dict): the dictionary to be used
        """
        for key, value in json:
            setattr(self, key, value)
