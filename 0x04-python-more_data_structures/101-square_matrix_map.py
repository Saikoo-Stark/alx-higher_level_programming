#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda inner: list(map(lambda key: key*key,
                                           inner)), matrix))
