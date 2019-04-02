#!/usr/local/bin/python

import fileinput
import glob
import re
import sys

if (len(sys.argv)) == 1:
    sys.argv += glob.glob('*.py')

print('checking:', sys.argv[1:], end='\n\n')

pattern = re.compile(r';\s*$')

outlist = open('semicolon.list', 'w')

for line in fileinput.input():
    if pattern.search(line):
        print('{:15s}{:3d} {:s}'.format(
            fileinput.filename(), fileinput.filelineno(), line), end='')
        print(fileinput.filename(), file=outlist)
