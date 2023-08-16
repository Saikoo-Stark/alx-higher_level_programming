#!/usr/bin/python3
def square_matrix_simple(mat=[]):
    matrix = mat.copy()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j]**2
