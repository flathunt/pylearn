#!/usr/local/bin/python

import os
import sys
import time

# Note: Use with data.txt/tail-f-demo.py?

if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
    infile = sys.argv[1]
else:    
    print("Usage: tail-f.py filename", file=sys.stderr)

fo = open(infile)

while True:
    line = fo.readline()
    
    if not line:
        time.sleep(1)
        fo.seek(fo.tell())
    else:
        print(line, end="")
