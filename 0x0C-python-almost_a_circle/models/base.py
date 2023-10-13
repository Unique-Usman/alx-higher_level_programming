#!/usr/bin/python3
"""Base class"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries:

        Args:
            list_dictionaries (list): List of dictionary
        Returns:
            str: The json string representation of the  list_dictionaries(arg)
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the string repesenation of the object to a file

        Args:
            list_objs (list): the list represetation of list_objs to a file
        """

        with open(f"{cls.__name__}.json", "w") as fd:
            json_rep = []
            if list_objs is None:
                json.dump(json_rep, fd)
            else:
                for obj in list_objs:
                    json_rep.append(obj.to_json_string(obj.to_dictionary()))
                json.dump(json_rep, fd)
