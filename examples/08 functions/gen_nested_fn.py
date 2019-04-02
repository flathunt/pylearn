#!/usr/local/bin/python

# Generates nested function definitions (limit seems to be 99)...

import sys

max = int(sys.argv[1])

for i in range(0, max):
    namechr = i + 97
    print('    ' * i, f'def {namechr:c}():', sep='')

print('    ' * max, 'print("Here!")', sep='')

for i in range(max-1, -1, -1):
    callchr = i + 97
    print('    ' * i, f'{callchr:c}()', sep='')
