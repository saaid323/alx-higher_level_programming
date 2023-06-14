#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = list(a_dictionary.keys())
        largest = 0
        name = ''
        for i in new:
            if a_dictionary[i] > largest:
                largest = a_dictionary[i]
                name = i
        largest = max(list(a_dictionary.keys()))

        return name
