#!/usr/bin/python3
def roman_to_int(roman_string):
    r_dict = {"X": 10, "V": 5, "I": 1, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    pre = 0
    if isinstance(roman_string, str):
        for i in roman_string[::-1]:
            value = r_dict[i]
            if value < pre:
                total -= value
            else:
                total += value
            pre = value
        return total
    return 0
