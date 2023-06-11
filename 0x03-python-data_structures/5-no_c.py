#!/usr/bin/python3
def no_c(my_string):
    b = []
    c = None
    for i in my_string:
        if i != "c" and i != "C":
            b.append(i)
        c = "".join(b)
    return c
