#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """print class in dict form

    Returns:
        dict: return __dict__ of the file
    """
    return obj.__dict__
