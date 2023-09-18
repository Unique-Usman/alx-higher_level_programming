#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """it writes to a file

    Args:
        filename: the name of file tp write to
        text: contain what we want to write to the file
    Returns:
        the number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as fd:
        num_of_char = fd.write(text)
    return num_of_char
