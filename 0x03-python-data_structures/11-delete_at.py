#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    elif my_list is None or len(my_list) == 0:
        return my_list

    n_list = my_list
    del n_list[idx]

    return n_list
