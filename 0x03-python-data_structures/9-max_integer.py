#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None
    m_max = my_list[0]
    for i in my_list:
        if m_max < i:
            m_max = i
    return m_max
