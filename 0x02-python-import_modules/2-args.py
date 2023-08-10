#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    args = len(argv)-1
    a = 's' if args > 1 or args == 0 else ''
    b = ':' if args > 0 else '.'
    print("{} argument{}{}".format(args, a, b))
    for a, b in enumerate(argv[1:]):
        print("{}: {}".format(a+1, b))
