#!/usr/local/bin/python
"""
    Utility module with functions 
    to calculate the area of common 2D shapes
"""    
   
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
    
def main():
    print('Area of circle, radius 10 =', circle(10))
    print('Area of triangle, base 8, height 3 =', triangle(8,3))
    print('Area of 6x9 rectangle =', rectangle(6,9))

    
if __name__ == '__main__':  
    main()
