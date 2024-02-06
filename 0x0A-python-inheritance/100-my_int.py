#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __int__(self, value: int):
        super().__int__(value)

    def __eq__(self, __value: int) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
