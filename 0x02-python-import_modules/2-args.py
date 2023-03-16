#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    length = len(argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("{} argument:".format(length), end='\n')
        print("{}: {}".format(length, argv[1]))
    else:
        print("{} arguments:".format(length), end='\n')
        for i in range(length):
            print("{}: {}".format((i+1), argv[i+1]), end='\n')
