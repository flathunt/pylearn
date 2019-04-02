#!/usr/local/bin/python

fruitlist = ['apple', 'pear', 'orange', 'kumquat', 'mango']

fruit = 'lime'
#fruit = 'pear'

try:
    fruitlist.remove(fruit)
    print('after', fruitlist)
except ValueError:
    print('No', fruit, 'here!')

    





