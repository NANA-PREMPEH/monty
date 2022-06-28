#!/usr/bin/python3
for numbers in range(100):
    if (numbers != 99):
        print("{}{}, ".format(int(numbers / 10), numbers % 10), end="")
    else:
        print("{}{}".format(int(numbers / 10), numbers % 10))
