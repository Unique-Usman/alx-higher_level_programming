#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """A class to make rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init function just l ike constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        Rectangle.number_of_instances += 1
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate thee area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle

        Returns:
            int: return the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """It speicifies what to be called when this class instance is printed

        Returns:
            str: it returns a string representation of each 0bject
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        ans = ""
        for i in range(self.__height):
            for j in range(self.__width):
                ans += f"{self.print_symbol}"
            ans += "\n" if i + 1 < self.__height else ""
        return ans

    def __repr__(self):
        """It returns the formal representation of the obj

        Returns:
            str: formal representation of the obj
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """The destructor is called when an object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """it check for the bigger rectangle

        Returns:
            Rectangle: rectangle that is bigger
        Raises:
            TypeError: if either of the rect obj is not
            and instance of rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() > rect_2.area() else rect_2
