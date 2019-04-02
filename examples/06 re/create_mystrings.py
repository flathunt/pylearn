#!/usr/local/bin/python

strings = (
    'apricot', 'actor', 'cap', 'cat', 'coat', 'coast', 
    'cold', 'colder', 'coldest', 'consented', 'coot', 'cot', 'cut', 'cutter', 
    'iouea', 'factory', 'rhythm', 'scatter', 'TDC327M', 'R2D2',
    'The cat sat...', 'another cat', 'a\ttabby\tcat', '0898')
    
with open('mystrings', 'w') as out:
    for item in strings:
        print(item, file=out)
