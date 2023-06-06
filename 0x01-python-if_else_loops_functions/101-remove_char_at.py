#!/usr/bin/python3
def remove_char_at(str1, n):
    count = 0
    m = []
    for i in str1:
        if count != n:
            m.append(i)
        count += 1
    return "".join(m)
