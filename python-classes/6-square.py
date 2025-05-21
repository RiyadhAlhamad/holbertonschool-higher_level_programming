#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """Represents the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.


        Args:
            size (int): the size of the square.
            position tuple: the position the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__position = position
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

    @property
    def position(self):
        """Return: position"""
        return self.position

    @position.setter
    def position(self, value):
        """Setter for set position"""
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) and not isinstance(valut[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print the Square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
