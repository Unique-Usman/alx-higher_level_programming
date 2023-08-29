#!/usr/bin/python3


class Square:
    """A class for making a square

    Attributes:
        size: __size of the any square object
        position: position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """It initialize any object of the class

        Args:
            size: the size of the side of the square
            position: position of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not == tuple and len(value) == 2:
            raise TypeError("position must be a tuple of 2 position integers")

    @size.setter
    def size(self, value):
        """for setting size attribute"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print the square with #

        Returns:
            nothing
        """

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        print("")
