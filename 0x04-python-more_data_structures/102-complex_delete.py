#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = a_dictionary.copy()
    for i in a.keys():
        try:
            if a_dictionary[i] == value:
                del a_dictionary[i]
        except Exception as e:
            pass
    return a_dictionary
