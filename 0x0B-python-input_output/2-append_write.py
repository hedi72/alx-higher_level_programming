#!/usr/bin/python3
"""
Contains the definition of the append_write function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of the text file and returns the
       number of chars written
    """

    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
