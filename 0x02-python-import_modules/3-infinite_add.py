#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='top',
        description='addition of all arguments')

    parser.add_argument('sum', type=int, nargs="*")

    args = parser.parse_args()
    total = 0
    for i in args.sum:
        total += i
    print(total)
