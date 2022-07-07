#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    den = 0

    for tuple in my_list:
        number += tuple[0] * tuple[1]
        den += tuple[1]

    return (number / den)
