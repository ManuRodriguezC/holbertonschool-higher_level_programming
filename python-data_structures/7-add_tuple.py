#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    for one in range(len(a)):
        for two in range(len(b)):
            a[one] + 0
            b[two] + 0
            if one == two:
                a[one] += b[two]
    tuple_a = tuple(a)
    return tuple_a
