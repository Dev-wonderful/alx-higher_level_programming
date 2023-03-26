def new_in_list(my_list, idx, element):
    n_list = [*my_list]
    id_len = len(my_list) - 1
    if idx > id_len or idx < 0:
        return n_list
    n_list[idx] = element
    return n_list
