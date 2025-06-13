#!/usr/bin/python3
"""
Module that contains class_to_json function
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: an instance of a Class

    Returns:
        dict: dictionary representation of the object's attributes
    """
    return obj.__dict__
