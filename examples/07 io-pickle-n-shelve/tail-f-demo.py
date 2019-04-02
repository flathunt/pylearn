#!/usr/local/bin/python

"""
Assuming tail-f.py has been invoked as:

tail-f.py data.txt

...and data.txt exists with, initially, three lines:

line1
line2
line3

...then this will ten add lines as:

line4
...

...for each execution.
"""

import os
import sys
import time

infile = 'data.txt'

with open(infile) as lines:
    start = len(lines.readlines()) + 1

with open(infile, 'a') as fo:
    for i in range(start, start + 10):
        print(f'line{i:d}', file=fo, flush=True)
        time.sleep(1)
