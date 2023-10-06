#!/usr/bin/python3
"""The rectangle class

The rectangle class inherit from the Base class
"""
from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width property getter

        Returns:
            int: the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width property setter

        Args:
            value (int): the width to set the width to
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property getter

        Returns:
            int: the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter

        Args:
            value (int): the height to set the height to
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x property getter

        Returns:
            int: the x of a rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x property setter

        Args:
            value (int): the x to set the x to
        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property getter

        Returns:
            int: the y of a rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y property setter

        Args:
            value (int): the x to set the x to
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

