"""This is a print module

>>> print_name("usman")
usman
"""


def print_name(name):
    """this print name which has to be a string

    >>> print_name("Fawaz")
    Fawaz
    >>> print_name(43)
    Traceback (most recent call last):
        ...
    TypeError: This only accept str
    """
    if type(name) is not str:
        raise TypeError("This only accept str")
    print(name)
