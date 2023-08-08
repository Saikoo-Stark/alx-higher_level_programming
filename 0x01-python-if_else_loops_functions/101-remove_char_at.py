#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    lst = list(str)
    for i in range(n, len(lst)-1):
        lst[i] = lst[i+1]
    lst.pop()
    return ''.join(lst)


# print(remove_char_at("Best School", 3))
# print(remove_char_at("Chicago", 2))
# print(remove_char_at("Chicago", 6))
# print(remove_char_at("C is fun!", 0))
# print(remove_char_at("School", 10))
# print(remove_char_at("Python", -2))
