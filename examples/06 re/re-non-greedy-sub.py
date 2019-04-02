#!/usr/local/bin/python

import re

sentences = (
    'The cat sat on the mat.',
    'The coot stood on the carpet.',
    )

for sentence in sentences:
    result = re.sub('c.*t', 'aardvark', sentence, count=1)
    print(result)
    
# Use 'c.*?t' to make non-greedy...     
