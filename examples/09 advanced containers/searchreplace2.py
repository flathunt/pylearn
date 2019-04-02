#!/usr/local/bin/python

# Demo dictionary comprehension from list of lists...

import re

srlines = [i.split() for i in open('sr.tab')]
srdict = {k:v for k, v in srlines}

# srdict = {k:v for k, v in [i.split() for i in open('sr.tab')]}
# srdict = {k:v for k, v in (i.split() for i in open('sr.tab'))}

print(srlines, srdict, sep='\n')

msg = "Pepsi, more pepsi, give me PEPSI!!!";

search = '|'.join(srdict.keys())
newmsg = re.sub(search, lambda m: srdict[m.group(0)], msg)

print(newmsg)
