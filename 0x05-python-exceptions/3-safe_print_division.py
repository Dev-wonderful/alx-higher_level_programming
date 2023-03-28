#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result += a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result if result else None))