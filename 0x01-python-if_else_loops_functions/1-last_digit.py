#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

result = str(number)

if number > 0:
    result = number % 10
    if result < 6 and result != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, result))
    elif result > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, result))
    else:
        print("Last digit of {} is 0 and is 0".format(number))
else:
    m = int(result[-1]) * -1
    if m < 6 and m != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, m))
    else:
        print("Last digit of {} is 0 and is 0".format(number))
