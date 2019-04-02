#!/usr/local/bin/python

import re

strings = (
    'apricot', 'actor', 'cap', 'cat', 'coat', 'coast', 
    'cold', 'colder', 'coldest', 'consented', 'coot', 'cot', 'cut', 'cutter', 
    'iouea', 'factory', 'rhythm', 'scatter', 'TDC327M', 'R2D2',
    'The cat sat...', 'another cat', 'a\ttabby\tcat', '0898')
    
for item in strings:
    if re.search('c.*t', item):       # also re.match() and re.fullmatch()
        print(item)
