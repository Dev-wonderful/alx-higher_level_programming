#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n_last = number % -10
    print(f"Last digit of {number} is {n_last} and is less than 6 and not 0")
else:
    last = number % 10
    if last <= 5 and last != 0:
        str = "Last digit of {} is {} and is less than 6 and not 0"
        print(str.format(number, last))
    elif last == 0:
        print("Last digit of {} is {} and is 0".format(number, last))
    else:
        str = "Last digit of {} is {} and is greater than 5"
        print(str.format(number, last))
