#!/usr/bin/python3
"""Define my custom class int"""

class MyInt(int):
    """my int class"""
    def __eq__(self, other):
        """Invert the behavior of ==

        Returns:
            bool: the inverted version
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the behavior of !=

        Returns:
            bool: the inverted version
        """
        return super().__eq__(other)
