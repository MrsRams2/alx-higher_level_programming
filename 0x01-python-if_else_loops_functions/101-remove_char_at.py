#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    a = 0
    for c in str:
        if a != n:
            new += c
        a += 1
    return new
