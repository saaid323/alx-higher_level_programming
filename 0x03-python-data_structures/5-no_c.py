#!/usr/bin/env python3
def no_c(my_string):
    b = []
    for i in my_string:
        if i != "c" and i != "C":
            b.append(i)
    return "".join(b)
