#!/usr/bin/python3
import sys


def main():
    size = len(sys.argv) - 1
    sum = 0
    for i in range(1, size + 1):
        sum += int(sys.argv[i])
    print(sum)

if __name__ == "__main__":
    main()
