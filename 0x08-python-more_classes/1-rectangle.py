#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """A class to make rectangle"""

    def __init__(self, width=0, height=0):
        """init function just l ike constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve the width of the rectangle

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width of the triangle

        Args:
            value (int): the value to set the rectangle width to
        """
        self.__width = value

    @property
    def height(self):
        """to retrieve the height of the rectangle

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """to set the height of the triangle

        Args:
            value (int): the value to set the rectangle height to
        """
        self.__height = value
