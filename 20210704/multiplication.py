#!/bin/env python3


i = 1
print("-" * 107)
while i < 10:
    n = 1
    while n <= i :
        print("{:2d} x{:2d} = {:2d}".format(n, i, i*n), end = ' ')
        n += 1
    i += 1
    print()
print("-" * 107)
