#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except Exception as e:
        pass
    return a_dictionary
