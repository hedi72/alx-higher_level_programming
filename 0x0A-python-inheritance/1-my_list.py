#!/usr/bin/python3
"""
contains the definition for the class MyList
"""


class MyList(list):
    """definition of class mylist"""

    def print_sorted(self):
        """print list sorted in ascending order"""

        print(sorted(self))
