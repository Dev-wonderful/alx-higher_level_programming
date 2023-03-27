#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst = [0] * 2
    id_x = 0
    id_y = 0

    if tuple_a is None or tuple_b is None:
        return

    for i in tuple_a:
        if i:
            lst[id_x] = i
        else:
            lst[id_x] = 0
        id_x += 1
        if id_x == 2:
            break

    for j in tuple_b:
        if j:
            lst[id_y] += j
        else:
            lst[id_y] += 0
        id_y += 1
        if id_y == 2:
            break

    f_tuple = (lst[0], lst[1])

    return f_tuple
