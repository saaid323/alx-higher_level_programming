#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        largest = max(list(a_dictionary.keys()))

        return largest
    return None
