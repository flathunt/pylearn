#!/usr/local/bin/python

def to_numeric(n):
    result = None
    try:
        result = int(n)
    except ValueError:
        try:
            result = float(n)
        except ValueError: 
            pass
            
    return result
       
inval = None

while inval != '':
    inval = raw_input(':')
    outval = to_numeric(inval)
    print(inval, outval, type(outval))
    
       
 
