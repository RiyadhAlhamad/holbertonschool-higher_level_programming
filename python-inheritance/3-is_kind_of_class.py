#!/usr/bin/python3
"""Module that defines function is kind of class."""


def is_kind_of_class(obj, a_class):
    """Return: The boolean if obj is instance of a_class or not

        Args:
            boolean: to return boolean loge False or True
    """
    boolean = False
    if isinstance(obj, a_class):
        boolean = True
    return boolean
