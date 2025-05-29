#!/usr/bin/python3
"""Module that defines empty class BaseGeometry."""


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """fun __init__ that instantiation with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
