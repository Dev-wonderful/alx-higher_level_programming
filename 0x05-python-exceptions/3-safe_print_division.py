#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if isinstance(a, int) and isinstance(b, int):
            result += a / b
            return result
        else:
            assert()
    except ArithmeticError:
        return None
    except AssertionError:
        return None
    finally:
        print("Inside result: {}".format(result if result else None))
