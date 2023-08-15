#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys


def main():
    """My calculator"""

    operator = ["+", "-", "*", "/"]
    size = len(sys.argv) - 1
    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if sys.argv[2] == "+":
        ans = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "-":
        ans = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "/":
        ans = div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        ans = mul(int(sys.argv[1]), int(sys.argv[3]))
    print("{} {} {}  = {}".format(sys.argv[1], sys.argv[2],  sys.argv[3], ans))


if __name__ == "__main__":
    main()
