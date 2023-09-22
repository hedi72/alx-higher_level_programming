#!/usr/bin/python3
"""
Contains definition of the class Base
"""


class Base:
    """Base class - base class of all classes in this project
                  - manage id attribute in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance of class Base

        Args:
            id (int): id value for id attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
