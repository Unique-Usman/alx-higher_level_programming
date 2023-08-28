#!/usr/bin/python3


def safe_print_division(a: int, b: int) -> float:
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result
