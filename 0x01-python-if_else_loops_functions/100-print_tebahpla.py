#!/usr/bin/python3

j = 0
for i in reversed(range(97, 123)):
    print("{}".format(chr(i) if j % 2 == 0 else chr(i - 32)), end="")
    j += 1
