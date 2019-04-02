#!/usr/local/bin/python
"""
    Utility module with functions 
    to calculate the area of common 2D shapes
    
    >>> c = circle(10)
    >>> print('{:6.3f}'.format(c))
    314.159
    
    >>> t = triangle(8,3)
    >>> print(t)
    12.0
    
    >>> r = rectangle(9,6)
    >>> print(r)
    54
   
    >>> p = _indiana_pi()
    >>> print(p)
    3
    
"""

# Note: run as areatest.py -v NOT python -v areatest.py

import math

def circle(radius):
    """
    Calculates the area of a circle.
    """
    area = math.pi * radius ** 2
    return area

def triangle(base, height):
    """
    Calculates the area of a triangle.
    """
    area = base * height / 2
    return area
    
def rectangle(width, height):
    """
    Calculates the area of a rectangle.
    """
    area = width * height
    return area 
    
def _indiana_pi():
    """
    See https://en.wikipedia.org/wiki/Indiana_Pi_Bill
    """ 
    return 3
 
 
if __name__ == '__main__':  
    import doctest
    doctest.testmod()
