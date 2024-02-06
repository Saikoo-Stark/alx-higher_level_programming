#!/usr/bin/python3
import sys
"""access commandline arguments"""
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""create object from JSON file"""
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""writes an object to text file, using JSON representation"""


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

with open("add_item.json", "a") as _:
    try:
        i = load("add_item.json")
    except ValueError:
        i = []
    save(i + sys.argv[1:], "add_item.json")
