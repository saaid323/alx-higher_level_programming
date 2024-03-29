#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers. """
    peak = None
    if list_of_integers is None or list_of_integers == []:
        return None
    li = list_of_integers
    for i in range(1, len(list_of_integers) - 1):
        if li[i] > li[i + 1] and  li[i] > li[i - 1]:
            peak = li[i]
    if li and peak is None:
        peak = li[0]
    return peak
