#!/usr/bin/python3
def uppercase(s):
    u = ""
    for c in s:
        if c > chr(ord('z')) or c < chr(ord('a')):
            u += "".join(c)
        else:
            u += "".join(chr(ord(c) - 32))
    print("{}".format(u))
