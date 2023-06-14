#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = my_list[:]
    for element in new_matrix:
        if element == search:
            new_matrix[element] = replace
    return  new_matrix
