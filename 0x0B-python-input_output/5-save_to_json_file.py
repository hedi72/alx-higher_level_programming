#!/usr/bin/python3
"""
Contains the definition of the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation
    """

    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
