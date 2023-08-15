#!/usr/bin/python3
import sys


def main():
    size = len(sys.argv) - 1
    print("{} argument{}{}".format(
        size,
        "",
        "s" if size == 1 else "",
        "." if size == 0 else ":"
    ))
    if size != 0:
        for i in range(1, size + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
