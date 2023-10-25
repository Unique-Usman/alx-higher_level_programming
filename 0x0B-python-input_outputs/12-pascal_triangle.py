#!/usr/bin/python3
"""a pascal triangle function"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def pascal_triangle(n):
    """return a list of integer rep pascal_triangle

    Args:
        n (int): the integer representing pascal triangle
    Returns:
        list: the list representing the pascal triangle
    """
    if n <= 0:
        return []
    res = []
    for i in range(1, n + 1):
        tmp = []
        for j in range(i):
            if j == 0:
                tmp.append(1)
            else:
                tmp.append(int(tmp[j - 1] * (i - j) / j))
        res.append(tmp)
    return res
