#!/usr/bin/python3
def uppercase(str):
    for i in str:
        s = ord(i)
        if s > 96:
            s = s - 32
        
        print("{:c}".format(s),end = "")
    print()
