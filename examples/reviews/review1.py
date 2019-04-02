#!/usr/local/bin/python

# What is the type of each object?
# Which are containers?
# Which are sequences?
# Is each type mutable or immutable?

a = 1

b = 6.02214e23

c = 'The cat sat on the mat.'

d = ['apple', 'orange', 'lime']

e = (5, 4, 3, 2, 1)

f = {'Ford': 'blue', 'Volvo': 'blue', 'Skoda': 'green'}

g = {'circle', 'triangle', 'square'}

print()
for item in a, b, c, d, e, f, g:
    print(type(item), item, sep='\t\t', end='\n\n')


# d[1] = 'tangerine'
# f['Mercedes'] = 'Silver'
# e[0] = 99
