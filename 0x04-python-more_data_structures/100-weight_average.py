#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    total_1 = 0
    if len(my_list) != 0:
        for i in my_list:
            total += i[0] * i[1]
            total_1 += i[1]
        return total / total_1
    return 0
