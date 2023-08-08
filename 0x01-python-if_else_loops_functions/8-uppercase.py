#!/usr/bin/python3
def uppercase(str):
    print("""{}""".format(''.join(chr(
        ord(i)-(ord('a')-ord('A'))
        )if ord(i) - ord('a') >= 0 else i for i in str)))
