#!/usr/local/bin/python

# TODO: define function here...

rectangles = ((9,6), (5,4), (7,9))

for width, height in rectangles:
    area = area_rectangle(width, height)
    print(f'{width:d} x {height:d} rectangle = {area:5.2f}')





# def area_rectangle(width, height):
#     result = width * height
#     return result    
