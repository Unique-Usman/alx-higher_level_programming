#!/usr/bin/python3
"""A Student class"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """The init function

        Args:
            first_name (str): the first_name
            last_name (str): the last_name
            age (int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """change the class to student

        Returns:
            dict: the dictionary representation of the class
        """
        return self.__dict__
