#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set = set()
    for i in set_1:
        if i not in set_2:
            unique_set.add(i)
    for j in set_2:
        if j not in set_1:
            unique_set.add(j)
    
    return unique_set
