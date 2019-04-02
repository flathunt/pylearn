#!/usr/local/bin/python

import re

strings = [
    'apricot', 'actor', 'cap', 'cat', 'coat', 'coast', 
    'cold', 'colder', 'coldest', 'consented', 'coot', 
    'my ip is 192.168.1.125', 'cot', 'cut', 'cutter', 
    'iouea', 'factory', 'rhythm', 'scatter', 'TDC327M', 'R2D2',
    'localhost is 127.0.0.1', 'Pi is roughly 3.14', 'Python 3.6.0',
    'The cat sat...','another cat','a\ttabby\tcat', '0898']
    
ip_pattern = r'\b(\d{1,3}\.){3}\d{1,3}\b'    
    
for index, item in enumerate(strings):
    if re.search(ip_pattern, item):
        print(item)
        
    new_item, changes = re.subn(ip_pattern, '...', item)
    if changes:
        strings[index] = new_item
        
print(strings)
