#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    for s in my_string:
        if s == "c" or s == "C":
            new_string += "".join("")
        else:
            new_string += "".join(s)
    return new_string
