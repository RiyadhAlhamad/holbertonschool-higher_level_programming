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

    def __eq__(self, value):
        """This for compare 2 squares and return is the size of 2 squares is equal"""
        return self.area() == value.area()

    def __ne__(self, value):
        """This for compare 2 squares and return is the size of 2 squares is not equal"""
        return self.area() != value.area()

    def __gt__(self, value):
        """This for compare 2 squares and return is the size of 2 squares is greater than"""
        return self.area() > value.area()

    def __lt__(self, value):
        """This for compare 2 squares and return is the size of 2 squares is less than"""
        return self.area() < value.area()

    def __ge__(self, value):
        """This for compare 2 squares and return is the size of 2 squares is greater or equal"""
        return self.area() >= value.area()

    def __le__(self, value):
        """This for compare 2 squares and return is the size of 2 squares is less or equal"""
        return self.area() <= value.area()
