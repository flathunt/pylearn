#!/usr/local/bin/python

# Demo...

import re

srdict = {
    'pepsi': 'irn-bru',
    'Pepsi': 'Irn-bru',
    'PEPSI': 'WATER'
}

msg = "Pepsi, more pepsi, give me PEPSI!!!";

search = '|'.join(srdict.keys())
new_msg = re.sub(search, lambda m: srdict[m.group(0)], msg)

print(new_msg)
