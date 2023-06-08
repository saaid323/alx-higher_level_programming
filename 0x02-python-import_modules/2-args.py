#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='top',
        description='Show top lines from each file')

    parser.add_argument('filename', nargs="*")

    args = parser.parse_args()
    n = len(args.filename)
    m = args.filename
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        for i in range(n):
            print("1: {}".format(args.filename[i]))
    else:
        print("{} arguments:".format(n))
        for i in range(n):
            print("{}: {}".format(i + 1, args.filename[i]))
