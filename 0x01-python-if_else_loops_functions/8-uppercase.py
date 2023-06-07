#!/usr/bin/python3
def uppercase(str):
    for i in str:
        s = ord(i)
        if s > 96:
            print("{:c}".format(s - 32),end = "")
        else:
            print("{:c}".format(s),end = "")
    print()
