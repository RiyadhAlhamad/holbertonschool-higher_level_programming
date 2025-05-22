#!/usr/bin/python3
"""Module that defines a class Rectangle"""


class Rectangle:
    """Represents a Rectangle with specific width and height"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the current width of Rectangle."""
        return self.__width

    @property
    def height(self):
        """Gets the cuttent height of Rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value for the width

            Args:
                value (int): new width of the Rectangle

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for the height

            Args:
                value (int): new height of the Rectangle

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return: The current area for the Rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Return: The current perimeter for the Rectangle."""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """print: object of the Rectangle.

            Args:
                result: For save the operation with width

            Return: For return the arg result to str()
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for _ in range(self.height):
                result += "#" * self.width + "\n"
            return result.rstrip()

    def __repr__(self):
        """Return: Should return a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print: message for user to delete rectangle."""
        print("Bye rectangle...")
