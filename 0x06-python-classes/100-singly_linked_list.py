#!/usr/bin/python3

"""Define a class that defines a node and SinglyLinkedList"""


class Node:
    """A node class"""

    def __init__(self, data, next_node=None):
        """Initialize the variable

        Args:
            data (int): data to be stored
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve the data attribute

        Returns:
            The data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """To set the data attribute to value

        Args:
            value (int): value to set the data to
        Raises:
            TypeError: value must be integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve the next_node attribute

        Returns:
            The next_node attribute
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """To set the new_node attribute to value

        Args:
            value (int): value to set the data to
        Raises:
            TypeError: value must be integer
        """
        if not isinstance(value, Node) or if not isinstance(value, None):
            raise TypeError("next_node must be a Node Object")
        next_node = value


class SinglyLinkedList:
    """A single linked list"""

    def __init__(self):
        """initialized the head"""
        __head = None

    def sortd_insert(self, value):
        """inserts a new Node"""
        if head == None:
            head = Node(value, None)
            return
        if head.next 
