#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list(items):
    """
    script that adds all arguments to a Python list, and
    then save them to a file
    """
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(items)
    save_to_json_file(existing_data, "add_item.json")


arguments = sys.argv[1:]
add_items_to_list(arguments)
