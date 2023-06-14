#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = my_list[:]
    for index, element in enumerate(new_matrix):
        if element == search:
            new_matrix[index] = replace
    return new_matrix
