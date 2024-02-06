#!/usr/bin/python3
"""
define append module
"""

import sys


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}
total_size = 0
r = 0
for line in sys.stdin:
    status, size = line.split()[7], line.split()[8]
    r += 1
    if status not in status_codes:
        continue
    total_size += int(size)
    status_codes[status] += 1
    if r == 10:
        print("File size: {}".format(total_size))
        for i, j in status_codes.items():
            if j != 0:
                print("{}: {}".format(i, j))
        r = 0
