#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    add = 0
    length = len(argv)

    if length == 1:
        print(0)
    else:
        for i in range(1, length):
            add += int(argv[i])
        print(add)
