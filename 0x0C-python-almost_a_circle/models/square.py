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

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """To find the dictionary representation of the square

        Returns:
            dict: The dictionary representation of the object
        """
        return {"id": self.id, "width": self.size,
                "x": self.x, "y": self.y
                }
