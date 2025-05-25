#!/usr/bin/python3
"""Module that defines a class Node with data and next_node."""

class Node:
    """Represents a Node with a specific data and next_node."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Square instance.

        Args:
            data (int): The data of the Node.
            next_node (int): The next_node for next node store pointer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the current data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the Node.

        Args:
            value (int): New data of the Node.

        Raises:
            TypeError: If value is not an integer.
        """
        if(not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the current next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node of the Node.

        Args:
            value (Node): The value resive the node (Node).

        Raises:
            TypeError: If value is not a Node object.
        """
        if(not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a SinglyLinkedList with attribute head."""

    __head = None

    def __init__(self):
        """Initialize a new SinglyLinkedList instance and pass."""
        pass

    def __str__(self):
        """Return: The newList of Node."""
        newList = []
        while(self.__head):
            newList.append(self.__head.data)
            self.__head = self.__head.next_node
        return("\n".join([str(x) for x in sorted(newList)]))

    def sorted_insert(self, value):
        """Sorted and insert new Node."""
        newNode = Node(value, self.__head)
        self.__head = newNode
