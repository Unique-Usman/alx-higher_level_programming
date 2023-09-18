#!/usr/bin/python3
"""add all arg to list and then save to json file"""
import sys
import json
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

data = sys.argv[1:]

if (os.path.exists("add_item.json")):
    with open("add_item.json", "r", encoding="utf-8") as fd:
        data = json.load(fd) + data

save_to_json_file(data, "add_item.json")
