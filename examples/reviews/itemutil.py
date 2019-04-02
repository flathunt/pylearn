#!/usr/local/bin/python

# This was used to re-cap on I/O, functions and advanced collections
# and as a preview of modules...

# (In Forres 14/5/2015)

infile = open('items.txt')

_itemlist = [ ln.rstrip('\n') for ln in infile.readlines() ]

infile.close()

def bysize(numchars):
    global _itemlist
    return [ th for th in _itemlist if len(th) == numchars ]
    
def byletter(letter):
    global _itemlist
    return [ th for th in _itemlist if th.startswith(letter) ]
       
#def oldbysize(numchars):
#    global _itemlist
#    result = []
#    
#    for th in _itemlist:
#        if len(th) == numchars:
#            result.append(th)
#    
#    return result
        
#print('Three letter words', bysize(3))
#print('Words starting with "e"', byletter('e'))

