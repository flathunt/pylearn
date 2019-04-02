#!/usr/local/bin/python

import re

sentences = (
    'The cat sat on the mat.',
    'The coot stood on the carpet.',
    )

for sentence in sentences:
    m = re.search('(.*?)c[oa]+t(.*)', sentence)
    pre, post = m.groups()

    # pre, post = re.split('c[oa]+t' , sentence)
    
    print('before:', pre, 'after:', post)
    

    

