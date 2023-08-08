#!/usr/bin/python3
# for i in range(ord('a'), ord('z')+1):
#     print(chr(i), end='')
print("{}".format(''.join([chr(i) for i in range(ord('a'), ord('z')+1)])), end='')
