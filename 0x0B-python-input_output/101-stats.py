#!/usr/bin/python3
import sys


for line in sys.stdin:
    line = line.split()
    code = []
    size = []
    size.append(line[8])
    code.append(line[7])
    count = code.count(line[7])
    print(line[7], ":", count)
    if len(code) % 10 == 0:
        print(sum(size))
