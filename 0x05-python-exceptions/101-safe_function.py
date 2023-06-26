#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as e:
        print("Exception:", e, file=sys.stderr)
    except IndexError as e:
        print("Exception:", e, file=sys.stderr)
