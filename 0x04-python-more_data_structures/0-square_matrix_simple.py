#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, 3):
        F = list(map(lambda x: x*x, matrix[i]))
        new_matrix.append(F)

    return new_matrix
