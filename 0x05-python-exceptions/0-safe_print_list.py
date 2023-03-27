#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter += 1
        print()
    except IndexError:
        print("Index doesn't exist")
    except:
        print("unknown Error")
    else:
        return counter
    finally:
        return counter