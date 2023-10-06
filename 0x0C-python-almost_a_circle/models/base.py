#!/usr/bin/python3
"""Base class"""


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """for initializing any instance

        Args:
            id (int): the id of the object:
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
