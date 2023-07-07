#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
     function that prints a text with 2 new lines after
     each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if i in ".,?:":
            flag += 1
            print(i, end='')
            print()
            print()
            continue
        if flag != 1 or i != ' ':
            print(i, end='')
        flag = 0
