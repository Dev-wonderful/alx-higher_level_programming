#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = [*my_list]
    idx = 0

    for i in lst:
        if i % 2 == 0:
            lst[idx] = True
        else:
            lst[idx] = False
        idx += 1
    return lst
