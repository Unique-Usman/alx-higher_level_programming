#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """A class for making a square"""

    def __init__(self, size=0):
        """It initialize any object of the class

        Args:
            size: the size of the side of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
