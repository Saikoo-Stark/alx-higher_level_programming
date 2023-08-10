#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    args = len(argv)-1
    print("{} argument{}{}".format(args, 's' if args > 1 or args == 0 else '', ':' if args > 0 else '.'))
    for a, b in enumerate(argv[1:]):
        print("{}: {}".format(a+1, b))
