#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if (i == j):
            continue
        elif (i * 10 + j == 89):
            print("{:02d}".format(i * 10 + j), end="\n")
        else:
            print("{:02d}".format(i * 10 + j), end=", ")
