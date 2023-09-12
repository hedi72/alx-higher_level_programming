#!/usr/bin/python3
"""
Contains the definition of the read_file function
"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    """

    with open(filename, encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
