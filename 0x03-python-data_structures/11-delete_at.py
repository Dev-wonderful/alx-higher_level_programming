#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list

    if my_list is None:
        return my_list

    n_list = my_list
    del n_list[idx]

    return n_list
