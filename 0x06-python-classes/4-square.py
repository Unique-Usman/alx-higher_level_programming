#!/usr/bin/python3


class Square:
    """A class for making a square

    Attributes:
        size: __size of the any square object
    """

    def __init__(self, size=0):
        """It initialize any object of the class

        Args:
            size: the size of the side of the square

        """
        self.size = size

    def area(self):
        """Returns the current square area

        Returns:
            The area of the square
        """

        return self.__size ** 2

    @property
    def size(self):
        """to retrieve size attribute

        Returns:
            size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """for setting size attribute

        Raises:
            TypeError: The size must be an integer
            ValueError: The size must be >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
