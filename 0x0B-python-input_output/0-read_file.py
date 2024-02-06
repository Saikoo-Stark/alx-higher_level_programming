#!/usr/bin/python3
"""
Defining class Mylist
"""


def read_file(filename=""):
    """ just a function"""
    with open(file=filename, mode="w", encoding="utf-8") as f:
        print(f.read())
