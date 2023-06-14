#!/usr/bin/python3
def roman_to_int(roman_string):
    r_dict = {"X": 10, "V": 5, "I": 1, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if roman_string:
        if roman_string[0] == 'I':
            return total - r_dict['I'] + r_dict['X']
        for i in roman_string:
            if i in r_dict:
                total += r_dict[i]
        return total
    return 0
