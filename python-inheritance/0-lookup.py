#!/usr/bin/python3
"""Module that defines a class Lookup"""


class Lookup():
    """Represents a Lookup"""

    def lookup(self, obj):
        return dir(obj)
