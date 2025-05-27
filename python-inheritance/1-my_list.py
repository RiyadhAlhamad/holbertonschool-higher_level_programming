#!/usr/bin/python3
"""Module that defines class MyList."""


class MyList(list):
    """defines class MyList."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)."""
        return print(sorted(self))