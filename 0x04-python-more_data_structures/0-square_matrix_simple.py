#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for row in matrix:
        F = list(map(lambda x: x * x, row))
        new_matrix.append(F)
    return new_matrix
