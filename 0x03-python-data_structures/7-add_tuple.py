#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ans = ()
    for i in range(2):
        first = (tuple_a[i] if len(tuple_a) >= i + 1 else 0) \
         + (tuple_b[i] if len(tuple_b) >= i + 1 else 0)
        ans = ans + (first, )
    return ans
