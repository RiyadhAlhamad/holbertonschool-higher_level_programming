#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle from BaseGeometry Class."""

    def __init__(self, width, height):
        """fun __init__ that instantiation with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
