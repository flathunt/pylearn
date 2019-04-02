#!/usr/local/bin/python

def area_rectangle(width, height):
    area = width * height
    return area   


dims = (8, 7)

res = area_rectangle(*dims)
print('area:', res)
    
dims = {'width':9, 'height':6}

res = area_rectangle(**dims)
print('area:', res)

    
    
