#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_new_dir = a_dictionary.copy()
    list_keys = list(my_new_dir.keys())

    for i in list_keys:
        my_new_dir[i] *= 2

    return (my_new_dir)
