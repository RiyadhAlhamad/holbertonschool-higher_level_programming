#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """Represents the square."""

    def __init__(self, size=0):
        """Initialize a new Square.


        Args:
            size (int): the size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the area of Square."""
        return self.__size * self.__size
