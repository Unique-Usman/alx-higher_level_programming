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


class Rectangle(BaseGeometry):
    """The rectangle"""

    def __init__(self, width, height):
        """to initialize the rectangle class

        Args:
            width (int): width of the triangle
            height (int): height of the triangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of the rectangle

        Returns:
            int: return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """overide the __str in string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
