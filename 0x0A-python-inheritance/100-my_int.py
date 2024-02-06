#!/usr/bin/python3
class MyInt(int):

    def __int__(self, value: int):
        super().__int__(value)

    def __eq__(self, __value: int) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
m