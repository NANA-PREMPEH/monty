#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_of_digit = number % 10
    else:
        last_of_digit = number % -10
        last_of_digit *= -1

    print("{:d}".format(last_of_digit), end='')
    return (last_of_digit)
