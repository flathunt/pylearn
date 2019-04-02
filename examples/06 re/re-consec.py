#!/usr/local/bin/python

import re

data = """
There is an operative word on this line.
How about a sentence including defenestration?
xxxxxxxxxxxx won't match.
As simple as ABC, or is it?
And lastly this one?
"""

pattern = '|'.join('{:c}(?={:c})'.format(i, i+1) for i in range(65, 90))

print(pattern)

for line in data.splitlines():
    for m in re.finditer(pattern, line, re.I):
        print(line, ' ' * m.start() + '==', sep='\n')
