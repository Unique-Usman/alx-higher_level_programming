#!/usr/bin/python3
"""The rectangle class

The rectangle class inherit from the Base class
"""
from .base import Base


class Rectangle(Base):
    """The class reactangle which inherit from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The init function

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x:
            y:
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width property getter

        Returns:
            int: the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width property setter

        Args:
            width (int): the width to set the width to
        """

        self.__width = width

    @property
    def height(self):
        """height property getter

        Returns:
            int: the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height property setter

        Args:
            height (int): the height to set the height to
        """

        self.__height = height

    @property
    def y(self):
        """y property getter

        Returns:
            int: the y of a rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y property setter

        Args:
            y (int): the x to set the x to
        """

        self.__y = y

    @property
    def x(self):
        """x property getter

        Returns:
            int: the x of a rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x property setter

        Args:
            x (int): the x to set the x to
        """

        self.__x = x
