#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """The function that reads a file

    Args:
        filename: the file to be read
    """
    with open(filename, "r", encoding="utf-8") as fd:
        for fileline in fd:
            print(fileline, end="")
