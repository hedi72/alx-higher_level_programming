#!/usr/bin/python3
"""
Contains the definition of the to_json_string function
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    """

    return json.dumps(my_obj)
