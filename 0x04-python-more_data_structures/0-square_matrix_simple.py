#!/usr/bin/python3
def square_matrix_map(m=[]):
    return list(map(lambda i: list(map(lambda key: key*key, i)), m))
