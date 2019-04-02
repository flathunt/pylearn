#!/usr/local/bin/python

import re
import sys

# Handle command line arguments...

if len(sys.argv) != 3:
    print("Usage: review2-search.py searchtermsfile datafile", file=sys.stderr)
    sys.exit(1)

terms_file, datafile = sys.argv[1:3]

# Read the file of search terms and build a RE pattern...

search_list = []
with open(terms_file) as search_words:
    for entry in search_words:
        search_list.append(entry.rstrip())

pattern = '|'.join(search_list)
# print('Pattern:', pattern, end='\n\n') # for debugging purposes

# Check the data file for matches...

with open(datafile) as data:
    for ln, line in enumerate(data, start=1):
        m = re.search(pattern, line)
        if m:
            print("{:04d} {:s}".format(ln, line), end='')
            print(' ' * (5 + m.start()) + '-' * (m.end() - m.start()))
