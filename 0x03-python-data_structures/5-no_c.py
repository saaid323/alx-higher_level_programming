#!/usr/bin/python3
def no_c(my_string):
    b = []
    new_string = None
    if my_string:
        for i in my_string:
            if i != "c" and i != "C":
                b.append(i)
            new_string = " ".join(b)
    return new_string
