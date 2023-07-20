#!/usr/bin/python3
"""
This module contains one function:

add_integer(a, b)
"""
def add_integer(a, b=98):
    """Add two integers
    Args:
        a(int):first intger
        b(int, optional):scond integer
    Returns:
        int: sum of two passed integers
    """
    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
