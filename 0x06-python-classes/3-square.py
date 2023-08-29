#!/usr/bin/python3


class Square:
    """A class for making a square

    Attributes:
        __size: __size of the any square object
    """

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


    def area(self):
        """Returns the current square area

        Returns:
            The area of the square
        """

        return self.__size ** 2
