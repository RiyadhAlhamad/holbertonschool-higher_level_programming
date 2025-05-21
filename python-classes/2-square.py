#!/usr/bin/python3
"""Class Square that defines a square.
   Reprsents a squate.
   private instance attribute: size.
   Instantation with size (no type/value verification)."""


class Square:
    """Initialize the square with a size"""

    def __init__(self, size=0):
        """must be an integer otherwise raise a TypeError"""
        try:
            size = int(size)
        except (ValueError, TypeError):
            raise TypeError("size must be an integer")

        """if size is less than 0 must raixe a valueError exception"""
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
