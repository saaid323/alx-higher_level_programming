#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import argparse

    parser = argparse.ArgumentParser(
                        prog='ProgramName',
                        description='What the program does',
                        epilog='Text at the bottom of help')

    parser.add_argument('numbers', nargs="*")

    args = parser.parse_args()

    op = ["+", "-", "*", "/"]

    if len(args.numbers) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args.numbers[1] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(args.numbers[0])
    b = int(args.numbers[2])
    if args.numbers[1] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if args.numbers[1] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if args.numbers[1] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    if args.numbers[1] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
