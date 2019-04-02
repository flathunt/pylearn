#!/usr/local/bin/python

import sys

var = input("Please enter an integer: ")

if var.isdecimal():
    var = int(var)
else:
    sys.exit(var + ' is not an integer')

for i in range(var, -1, -2):
    print(i)
