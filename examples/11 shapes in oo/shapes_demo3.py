#!/usr/local/bin/python

from circle import Circle


def pcircs():
    for c in c1, c2, c3:
        print(c, repr(c), c.radius, sep=' ; ')


c1 = Circle(10)
c2 = Circle(5)
c3 = c1 + c2
pcircs()

c1 += 10
c2 *= 3
c3 -= 1
c1.radius = 99
pcircs()

