#!/usr/local/bin/python

import re
import sys
import os

COLUMNS = 70        # two less than required line end, 'cos of comma 'n' space
DEMO = r"""
[aeiou]  [^aeiou]  [A-E]

.  \.  c.t  c.*t  c.+t  c.?t  c.{1,3}t  c[ao]+t  c(oa)?t

^c        t$        ^c.*t$

cat|st|ct           \s         \d	\d\D    ^\d+$

(... cat\b cat\B later?)
"""

if sys.platform == 'linux':
    os.system('clear')
else:
    os.system('cls')


def print_items(items):
    len_so_far = COLUMNS  # force line-break first time
    
    for i in items:
        quoted_item = "'" + i + "'"
        if len_so_far + len(quoted_item) < COLUMNS:
            print(', ', end='')
            len_so_far += len(quoted_item) + 2
        else:
            print()
            len_so_far = len(quoted_item)
            
        print(quoted_item, end="")
        
    print("\n")

strings = (
    'apricot', 'actor', 'cap', 'cat', 'coat', 'coast', 
    'cold', 'colder', 'coldest', 'consented', 'coot', 'cot', 'cut', 'cutter', 
    'iouea', 'factory', 'rhythm', 'scatter', 'TDC327M', 'R2D2',
    'The cat sat...', 'another cat', 'a\ttabby\tcat', '0898')

matches = []
non_matches = []


if len(sys.argv) == 1:
    print("\nStrings:")
    print_items(strings)
    print('\nPatterns:\n')
    print(DEMO)
    
else:
    print('\nPattern:', sys.argv[1], end='\n\n')
    pattern = re.compile(sys.argv[1])

    for s in strings:
        if pattern.search(s):
            matches.append(s)
        else:
            non_matches.append(s)

    print("Matches:")
    print_items(matches)
    print("Non-matches:")
    print_items(non_matches)

print('\n')
