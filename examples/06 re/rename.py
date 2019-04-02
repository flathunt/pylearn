#!/usr/local/bin/python

import os
import re
import sys

if len(sys.argv) != 4:
    sys.exit('Usage: rename.py filename search replace')

# run with filename txt bak...

name, old, new = sys.argv[1:]

new_name = re.sub(fr"\.{old}$", f".{new}", name)
print(f"Renaming {name} to {new_name}")
os.rename(name, new_name)



