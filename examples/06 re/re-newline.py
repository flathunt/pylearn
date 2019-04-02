#!/usr/local/bin/python

import re

# sentence = 'some string'
# sentence = 'Mary had a little lamb'
sentence = 'A line\nMary had a little lamb\nAnother line\n' # add (?m)
# sentence = 'Mary had\na little lamb' # add (?s)
# sentence = 'A line\nMary had\na little lamb\nAnother line\n' # add (?ms)

print('sentence:\n' + sentence)

if re.search('(?m)^M.*b$', sentence):
    print('Found')
else:
    print('No such value')
