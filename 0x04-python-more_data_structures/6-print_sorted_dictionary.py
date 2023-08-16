#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = dict(sorted(a_dictionary.items()))
    for i, j in dic.items():
        print(f"{i}: {j}")
