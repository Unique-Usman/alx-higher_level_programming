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

    def to_json(self, attrs=None):
        """change the class to student

        Args:
            attrs: can be list of string
        Returns:
            dict: the dictionary representation of the class
        """
        if type(attrs) is list:
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = (self.__dict__)[i]
            return res
        return self.__dict__
