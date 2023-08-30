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

    @next_node.setter
    def next_node(self, value):
        """To set the new_node attribute to value

        Args:
            value (int): value to set the data to
        Raises:
            TypeError: value must be integer
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node Object")
        self.__next_node = value


class SinglyLinkedList:
    """A single linked list"""

    def __init__(self):
        """initialized the head"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node"""
        tmp = Node(value)
        if self.__head is None or value < self.__head.data:
            tmp.next_node = self.__head
            self.__head = tmp
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            tmp.next_node = temp.next_node
            temp.next_node = tmp

    def __str__(self):
        """this function is called when the print function is used

        Returns:
            str: the element of each node in concatenate manner
        """
        res = ""
        tmp = self.__head
        while tmp:
            if tmp.next_node is None:
                res += str(tmp.data)
                tmp = tmp.next_node
                continue
            res += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return res
