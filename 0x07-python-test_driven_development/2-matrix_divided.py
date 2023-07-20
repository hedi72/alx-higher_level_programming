#!/usr/bin/python3
"""
This module contains one function:

matrix_divided(matrix, div) -> returns a new matrix
"""


def matrix_divided(matrix, div):
    ms1 = "matrix must be a matrix (list of lists) of integers/floats"
    ms2 = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(ms1)

   
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(ms2)

  
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

   
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
