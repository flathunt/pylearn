#!/usr/local/bin/python

from car import Car

c1 = Car('Hillman', 'Avenger', 'Gold', 'TDC327M')

c1.start()
print(c1.status)
print(c1, type(c1))

c1.colour = 'Beige'
print(c1)

c2 = Car('Vauxhall', 'Astra', 'Green', 'WRN193Y')
print(c2)

print(repr(c2))







































