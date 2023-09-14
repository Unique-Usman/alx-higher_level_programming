#!/usr/bin/python3
"""This module defines a function for addition"""


def add_integer(a, b=98):
    """function for adding two integers

    a and b can only be integers and float
    they must be typecasted to int before
    the operation

    Args:
        a (int): the first number
        b (int): the second number
    Raises:
        TypeError: a and b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
