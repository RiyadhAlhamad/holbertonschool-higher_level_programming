#!/usr/bin/python3
"""Module that defines empty class BaseGeometry."""


class BaseGeometry:
    """Empty class BaseGeometry."""

    def area(self):
        """fun that raise Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """fun that that validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
