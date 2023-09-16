#!/usr/bin/python3
"""This module list the attribute and method of a class"""


def lookup(obj):
    """list the method and attribute of a class

    Args:
        obj: the object to find it's attribute
    Returns:
        list: list of attribute and method of a class
    """
    return dir(obj)
