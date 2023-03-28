#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    result = 0
    try:
        result += a / b
    except (ArithmeticError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
