#!/usr/bin/python3
"""Module that defines function lookup with parmeters obj."""


def lookup(obj):
    """Return: The list of available attributes and methods of an object.
    Args:
        obj: instance of the class.

    Returns:
        List of attributes."""
    return dir(obj)
