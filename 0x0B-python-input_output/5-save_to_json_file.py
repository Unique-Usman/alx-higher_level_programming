#!/usr/bin/python3
"""write to json file"""
import json


def save_to_json_file(my_obj, filename):
    """write to a json file using json notation

    Args:
        my_obj: object to write to file
        filename: the name of file to write
    """
    with open(filename, "w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)
