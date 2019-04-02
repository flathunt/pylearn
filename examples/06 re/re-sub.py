#!/usr/local/bin/python

import re

sentence = 'The cat sat on the mat.'

result = re.sub('[cm]at', '***', sentence)

print(result)


# msg = 'MSG001 Error occurred on 02/05/2014'
# iso_date = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', msg)
# print(iso_date)


# result = re.subn('([aeiou])' , r'\1\1\1', sentence, 4)
# result = re.subn('([aeiou])' , r'\1\1\1', sentence, count=4)
# print(result)


# sentence = 'Mr. Cat sat on the mat.'
# result = re.sub('[cm]at' , '***', sentence, flags=re.IGNORECASE)
# result = re.subn('[cm]at' , '***', sentence)
# result = re.subn('C.*t' , 'Aardvark', sentence)
