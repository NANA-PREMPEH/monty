#!/usr/bin/python3
def islower(c):
    ascii_number_s = ord(c)
    if ascii_number_s >= 97 and ascii_number_s <= 122:
        return True
    return False
