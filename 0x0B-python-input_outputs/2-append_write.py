#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Append text to file

    Args:
        filename: the file that we wants to append to
        text: the text that we want to append
    Returns:
        the number of character written
    """
    with open(filename, "a", encoding="utf-8") as fd:
        num_of_char = fd.write(text)
    return num_of_char
