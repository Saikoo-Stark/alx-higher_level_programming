#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = dict(sorted(a_dictionary.items(), key=lambda item: item[0])
    for i, j in dic.items():
        print(f"{i}: {j}")
