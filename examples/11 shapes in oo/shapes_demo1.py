#!/usr/local/bin/python

from rectangle import Rectangle

r1 = Rectangle(width=9, height=6)
r2 = Rectangle(width=3, height=4)

print(id(r1), type(r1), r1.get_area())
print(id(r2), type(r2), r2.get_area())

print('making changes...')

r1.width = 10
r2.height = 8

print(id(r1), type(r1), r1.get_area())
print(id(r2), type(r2), r2.get_area())

