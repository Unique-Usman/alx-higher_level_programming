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

        if not isinstance(value, int):
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
        if not isinstance(value, int):
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

        if not isinstance(value, int):
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

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the area of the rectangle

        Returns:
            area (int): return the area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """Display the area of triangle in ###"""
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

            [print("") for i in range(self.__y)]
        for j in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            [print("#", end="") for i in range(self.__width)]
            print()
    def __str__(self):
        """returns a string representaion of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
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
                    self.width = arg
                elif a == 2:
                    self.height = arg
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
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """To find the dictionary representation of an object

        Returns:
            dict: The dictionary representation of the object
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y
                }
