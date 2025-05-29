#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square from Rectangle Class """

    def __init__(self, size):
        """ Initializes instance """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """return the super area"""
        return super().area()
