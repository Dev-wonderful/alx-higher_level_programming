#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result += a / b
    except (ArithmeticError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result if result else None))
    return result
