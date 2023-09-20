#!/usr/bin/python3
"""Append a line after a line containing a word"""


def append_after(filename="", search_string="", new_string=""):
    """append a new after a finding a string in a line

    Args:
        filename: the name of the file
        search_string: the str in sentence to insert after
        new_string: the string to insert
    """
    with open(filename, "r", encoding="utf-8") as fd:
        lines = fd.readlines()

    with open(filename, "w", encoding="utf-8") as fd:
        for line in lines:
            fd.write(line)
            if search_string in line:
                fd.write(new_string)
