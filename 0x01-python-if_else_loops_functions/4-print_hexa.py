#!/usr/bin/python3
for number in range(99 + 1):
    print("{} = {}".format(number, hex(number)), end="\n" if number == 99 else ", ")
