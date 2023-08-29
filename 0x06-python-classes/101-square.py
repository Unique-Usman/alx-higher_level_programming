#!/usr/bin/python3

"""Define a square"""


class Square:
    """A class for making a square"""

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
        """to retrieve the position attribute

        Returns:
            position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set position attrbute

        Return:
            return nothing
        Args:
            value: value of to set the position to
        Raises:
            TypeError: The value must be tuple with len 2
        """
        if not isinstance(value, tuple) and len(value) == 2:
            raise TypeError("position must be a tuple of 2 position integers")
        self.__position = value

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
            it returns nothing
        """

        if self.__size == 0:
            print("")
            return
        square_string = ""

        for _ in range(self.__position[1]):
            square_string += "\n"

        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size + "\n"
            square_string += line

        print(square_string)
    def __str__(self):
        """return the square with #

        Returns:
            it returns the string
        """

        if self.__size == 0:
            print("")
            return
        square_string = ""

        for _ in range(self.__position[1]):
            square_string += "\n"

        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size + "\n"
            square_string += line

        return square_string
