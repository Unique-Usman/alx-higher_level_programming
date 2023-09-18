#!/usr/bin/python3
"""add all arg to list and then save to json file"""
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

data = sys.argv[1:]
save_to_json_file(data, "add_item.json")
