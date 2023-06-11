#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    b = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            b.append(element)
        else:
            b.append(my_list[i])
    return b
