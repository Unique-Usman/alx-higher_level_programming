#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """calculate the area of the geometry

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value

        Args:
            name (str): name of what to validate
            value (int) : value to validate
        Raises:
            TypeError: value must be int
            ValueError: value must be greater than 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")


class Square(BaseGeometry):
    """The square"""

    def __init__(self, size):
        """to initialize the square class

        Args:
            size (int): size of the square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of the rectangle

        Returns:
            int: return the area of the rectangle
        """
        return self.__size ** 2
