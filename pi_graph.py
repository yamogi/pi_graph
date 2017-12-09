#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
passes = 9
num = 0
char = "┃"

print(pi)

for i in range(0, passes):                         # parse pi 10 times (0 to 9)
    for j in range(0, len(pi)):                    # each parse, check each character individually
        if (pi[j] == ".") or (int(pi[j]) <= num):  # if checked char is the decimal point or is <= number to check
            print(" ", end="")                     # print a space
        else:
            print(char, end="")                    # print a specific character

    num += 1  # increment the number to check
    print() # newline

print()  # newline
