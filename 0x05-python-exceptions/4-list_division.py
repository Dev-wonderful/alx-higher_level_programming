#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for div_cycle in range(list_length):
        try:
            new_list.append(my_list_1[div_cycle] / my_list_2[div_cycle])
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        finally:
            pass

        continue
    return new_list
