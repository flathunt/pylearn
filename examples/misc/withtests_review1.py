#!/usr/local/bin/python

import collections

a = 1
b = 6.02214e23
c = 'The cat sat on the mat.'
d = ['apple', 'orange', 'lime']
e = (5, 4, 3 ,2, 1)
f = {'Ford':'blue', 'Volvo':'blue', 'Skoda':'green'}
g = {'circle', 'triangle', 'square'}

print()
for item in a,b,c,d,e,f,g:
    print(type(item), item, sep='\t\t')
    print('Sequence?', isinstance(item, collections.Sequence), end='\n\n')

# Which are containers?
# Which are sequences?
# Is each type mutable or immutable?


# d[1] = 'tangerine'
# f['Mercedes'] = 'Silver'
# e[0] = 99

    
    
