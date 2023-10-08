#!/usr/bin/python3
"""The class square shape"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """The square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The initialization method

        Args:
            size (int): the size of the square
            x (int): the x
            y(int): the y
        """
        super().__init__(size, size, x, y)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """The size attribute getter

        Returns:
            int: the size of the square(width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set value of the size

        Args:
            value (int): the value to set the size to
        """
        self.width = value
