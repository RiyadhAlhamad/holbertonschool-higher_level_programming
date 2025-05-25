#!/usr/bin/python3
"""Module that defines a class Node."""


class Node:
    """Represents a Node."""

    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node."""
        self.__data = data
        self.__next_node = next_node

    @data.setter
    def data(self, value):
        """Setter value to data and check if (int) or not."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.data = value

    @next_node.setter
    def next_node(self, value):
        """Setter value to next_node and check if (Node) or not None."""
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.next_node = value

    @property
    def data(self):
        """Return: data."""
        return self.data

    @property
    def next_node(self):
        """Return: next node."""
        return self.next_node

class SinglyLinkedList:
    """Represents a SinglyLinkedList."""

    def __init__(self):
        self.__head = self
        print(self.__head)

    def sorted_insert(self, value):
        """Insert Node."""
        self.__head = value
