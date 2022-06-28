#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_strings = ""
    for ch in str:
        if i != n:
            new_strings += ch
        i += 1
    return new_strings
