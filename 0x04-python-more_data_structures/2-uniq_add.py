#!/usr/bin/python3
def uniq_add(my_list=[]):
    li = list(set(my_list))
    sum = 0
    for i in li:
        sum += i
    return sum
