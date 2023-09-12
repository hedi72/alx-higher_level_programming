#!/usr/bin/python3
"""
contains the definition of the write_file function
"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the numbers
    """

    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
