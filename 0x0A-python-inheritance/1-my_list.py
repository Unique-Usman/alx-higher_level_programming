#!/usr/bin/python3
"""A class that inherit from list class"""


class MyList(list):
    """MY custom class"""

    def print_sorted(self):
        """print the list in sorted(ascending sort)"""

        print(sorted(self))
