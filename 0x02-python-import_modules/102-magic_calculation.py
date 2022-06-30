#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add as addition, sub as subtraction
    if a < b:
        c = addition(a, b)
        for i in range(4, 6):
            c = addition(c, i)
        return (c)
    else:
        return (subtraction(a, b))
