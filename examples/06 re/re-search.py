#!/usr/local/bin/python

import re

sentence = 'The cat sat on the mat.'

m = re.search('[cm]at', sentence)
if m:
    print('Found', m.group(0))
    print(m.start(), m.end(), sep=', ')
else:
    print('Not found')
    
  
# Mr. Cat  ...       use re.I or (?i)  

# l = re.findall('[cm]at', sentence)
# print(l)


# for m in re.finditer('[cm]at', sentence):
#     print('Found', m.group(0), m.start())
