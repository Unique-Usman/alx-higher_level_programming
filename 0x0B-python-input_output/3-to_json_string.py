#!/usr/bin/python3
"""convert string to the json represenation"""
import json


def to_json_string(my_obj):
    """convert string to json represenation

    Args:
        my_obj (str): string representation
    Returns:
        JSON represenation of the string object
    """
    return json.dumps(my_obj)
