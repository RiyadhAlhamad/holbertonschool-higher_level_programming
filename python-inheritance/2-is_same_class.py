#!/usr/bin/python3
"""Module that defines function is same class with two attr"""


def is_same_class(obj, a_class):
    """Return: The boolean if obj is instance of a_class or not
 
        Args:
            boolean: to return boolean loge False or True
    """
    boolean = False
    if type(obj) is a_class:
        boolean = True
    return boolean
