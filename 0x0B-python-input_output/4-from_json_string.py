#!/usr/bin/python3
"""
Contains the definition of the from_json_string function
"""
import json


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON
    """

    return json.loads(my_str)
