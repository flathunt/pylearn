#!/usr/local/bin/python

from fileinput import input, filename

for line in input():
    print(filename(), ':', line, end='')
