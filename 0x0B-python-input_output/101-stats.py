#!/usr/bin/python3
"""
define append module
"""

import sys


status_op = ['200', '301', '400', '401', '403', '404', '405', '500']


statuses = {}
total_size = 0
r = 0
for line in sys.stdin:
    status, size = line.split()[7], line.split()[8]
    r +=1
    if status not in status_op:
        continue
    total_size += int(size)
    statuses[status] = statuses.get(status, 0) + 1
    if r == 10:
        print("File size: {}".format(total_size))
        for i, j in statuses.items():
            print("{}: {}".format(i, j))
        r = 0
