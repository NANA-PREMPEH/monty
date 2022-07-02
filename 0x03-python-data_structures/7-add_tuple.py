#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_len_a = len(tuple_a)
    my_len_b = len(tuple_b)

    if my_len_a == 0:
        a1 = 0
        a2 = 0
    elif my_len_a == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if my_len_b == 0:
        b1 = 0
        b2 = 0
    elif my_len_b == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    my_new_tuple = (a1 + b1, a2 + b2)

    return (my_new_tuple)
