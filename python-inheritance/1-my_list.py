#!/usr/bin/python3
"""Module that defines class MyList."""


class MyList(list):
    """defines class MyList."""

    def print_sorted(self):
        """def for print and sort list.
        Args:
            myList: tack a copy from list class and sorted.
        Return:
            return myList sorted.
        """
        myList = list.copy(self)
        myList.sort()
        return myList