#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(f"{my_list[i]:d}", end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
