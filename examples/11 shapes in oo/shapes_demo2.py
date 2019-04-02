#!/usr/local/bin/python

from shapecollection import ShapeCollection
from circle import Circle
from rectangle import Rectangle

rectangle_dims = ((9,6), (5,4), (7,9))
circle_dims = (9, 13, 5, 27)

sc = ShapeCollection()

c1 = Circle(9)
sc.add(c1)

for w, h in rectangle_dims:
    r = Rectangle(w, h)
    sc.add(r)
    
for r in circle_dims:    
    sc.add(Circle(r))
    
for s in sc:
    print(type(s), s.area)

print('\ntotal:', sc.area, 'no of shapes:', len(sc))
