#!/usr/bin/python3
"""Module that defines a class Lookup"""


class Lookup():
    """Represents a Lookup"""

    def lookup(self, obj):
        list = []
        for i in range(obj):
            for a in obj:
                list[i] = a
        return list
