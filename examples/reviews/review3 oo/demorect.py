#!/usr/local/bin/python

from rectangle_v2 import Rectangle

r1 = Rectangle(16, 9)

r2 = Rectangle(5, 4)

print(f'r1 ({r1.width}x{r1.height}) area is:', r1.get_area())

print(f'r2 ({r2.width}x{r2.height}) area is:', r2.get_area())

r2.width = 10

print(f'r2 ({r2.width}x{r2.height}) area is:', r2.get_area())


