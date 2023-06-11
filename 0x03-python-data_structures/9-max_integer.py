#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    if len(my_list) == 0:
        largest = None
    else:
        for i in my_list:
            if i > largest:
                largest = i
    return largest
