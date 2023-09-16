#!/usr/bin/python3
"""to check if an object is exactly the instance of another"""


def is_same_class(obj, a_class):
    """check if an object is an instance of a class

    Args:
        obj: object
        a_class: class
    Returns:
        bool: True if they are the same else false
    """

    return isinstance(obj, a_class)
