#!/usr/local/bin/python

import re
import sys

msg = 'MSG001 Error occurred on 02/05/2014'

m = re.search(r'(\d+)/(\d+)/(\d+)', msg)
print('groups:', m.groups())

print('date:  ', m.group(0))
print('day:   ', m.group(1))
print('month: ', m.group(2))
print('year:  ', m.group(3))

sys.exit()











search2 = r"""
(?x)                # allow whitespace and comment...
                    # look for dd/mm/yyyy

(\d+)               # capture day

/                   # match a forward slash

(\d+)               # capture month

/                   # match another forward slash

(\d+)               # capture year
"""

m = re.search(search2, msg)
print(m.groups())






