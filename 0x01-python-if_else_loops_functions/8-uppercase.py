#!/usr/bin/python3
def to_uper(best):
    if ord(best) >= 97 and ord(best) <= 122:
        return (ord(best) - 32)
    else:
        return ord(best)


def uppercase(str):
    new = ""
    for best in str:
        new += "%c" % to_uper(best)
    print("{:s}".format(new))
