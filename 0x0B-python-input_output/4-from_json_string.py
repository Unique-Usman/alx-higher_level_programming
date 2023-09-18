#!/usr/bin/python3
"""convert json to objecs"""
import json


def from_json_string(my_str):
    """from json to string

    Args:
        my_str: the json string
    Returns:
        it returns the str object
    """
    return json.loads(my_str)
