#!/usr/local/bin/python

import re

filename = 'home.eric.2014-11-01@10:50:33.tgz'

file_parts = re.split('[.@:-]', filename)

print(filename, file_parts, sep='\n')
