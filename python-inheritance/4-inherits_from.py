#!/usr/bin/python3
"""Module that defines function is kind of class."""


def inherits_from(obj, a_class):
    """Return: The boolean if obj is instance of a_class or not

        Args:
            boolean: to return boolean loge False or True
    """
    boolean = False
    if type(obj) is a_class:
        return boolean
    else:
        return isinstance(obj, a_class)
