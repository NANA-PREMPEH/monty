#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    my_new_list = my_list[:]

    if 0 <= idx < length:
        my_new_list[idx] = element

    return (my_new_list)
