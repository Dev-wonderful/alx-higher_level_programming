#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord("a"):
        print(chr(ord(c) - 32))
        return bool(1)
    else:
        return bool(0)
