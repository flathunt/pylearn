#!/usr/local/bin/python

from fileinput import input, filename
from glob import glob
import sys

# handle Windows 'globbing'...

if sys.platform == 'win32' and len(sys.argv) > 1:
    matches = []
    while len(sys.argv) > 1:
        matches += glob(sys.argv.pop(1))

    if matches:
        sys.argv += matches
    else:
        sys.exit()

# Process files...

for line in input():
    print(filename(), ':', line, end='')