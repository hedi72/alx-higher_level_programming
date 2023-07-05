#!/usr/bin/python3
"""Define a class Square."""


class Square:

    """ class square defines a square by size """
    def __init__(self, size=0):
        """ initialize square object """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """Return the current area of the square."""

        return (self.__size * self.__size)
