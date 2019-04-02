#!/usr/local/bin/python
import getprocs

   
###################################################################

def igetprocs():
    
    retn = getprocs.getfirstproc()
    first = True

    while retn or first:
        yield retn
        first = False
        retn = getprocs.getnextproc()
            
###################################################################

for proc in igetprocs():
    print(proc)
