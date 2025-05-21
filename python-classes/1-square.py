#!/usr/bin/python3
"""Class Square that defines a square.
   Reprsents a squate.
   private instance attribute: size.
   Instantation with size (no type/value verification)."""


class Square:
    """Initialize the square with a size"""

    def __init__(self, size):
        self.__size = size
