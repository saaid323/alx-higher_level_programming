#!/usr/bin/python3
def no_c(my_string):
    b = []
    c = None
    if my_string:
        for i in my_string:
            if i != "c" and i != "C":
                b.append(i)
            c = "".join(b)
    return c
