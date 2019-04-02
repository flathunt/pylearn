#!/usr/local/bin/python

# demo script for parameters w.r.to mutability

import sys

def multi(x):
    x *= 4
    return x

print('\nDemo:\n')

# Assign function result to variable passed in as arg...
    
mynumber = 99
mynumber = multi(mynumber)
print('mynumber value after :', mynumber, end='\n\n')

mylist = [3,2]
mulist = multi(mylist)
print('mylist value after :', mylist, end='\n\n')
    
sys.exit()

# Don't assign back ('void' context)...

mynumber = 99
multi(mynumber)
print('mynumber value after :', mynumber, end='\n\n')

mylist = [3,2]
multi(mylist)
print('mylist value after :', mylist, end='\n\n')
    
    
