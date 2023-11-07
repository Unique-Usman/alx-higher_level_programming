#!/usr/bin/python3
"""load object from file"""
import json


def load_from_json_file(filename):
    """load from file

    Args:
        filename: the name of the file to load from
    """
    with open(filename, "r", encoding="utf-8") as fd:
        file = json.load(fd)
    return file
