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
        self.__width = width
        self.__height = height

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
            raise ValueError("widht must be >= 0")
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
