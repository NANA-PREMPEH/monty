#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_division = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            check_division.append(True)
        else:
            check_division.append(False)

    return (check_division)
