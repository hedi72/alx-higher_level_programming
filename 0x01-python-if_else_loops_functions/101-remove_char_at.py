#!/usr/bin/python3
def remove_char_at(str, n):
    car = " "
    for i in range(len(str)):
        if i != n:
            car += str[i]
    return car
