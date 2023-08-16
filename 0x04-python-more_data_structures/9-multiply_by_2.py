#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dica = a_dictionary.copy()
    for i in dica.keys():
        dica[i] = dica[i]*2
    return dica
