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

    @property
    def size(self):
        """Return: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print the Square"""
        if self.__size == None:
            print()
        else:
            for i in range(self.__size):
                for a in range(self.__size):
                    print("#", end='')
                print()
