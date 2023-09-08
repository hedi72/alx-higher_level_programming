#!/usr/bin/python3
"""definition of the add_integer function"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
     a (int):first int
     b (int, optional): second int
     Returns:
       int: sum of twp passed integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
