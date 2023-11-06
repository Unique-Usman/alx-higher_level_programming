#!/usr/bin/python3
"""check if an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """check if an object is an instance has a superclass

    Args:
        obj: object
        a_class: super class
    Returns:
        bool: True if it has else false
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
