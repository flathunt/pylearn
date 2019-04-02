#!/usr/local/bin/python

items = \
  ['elephant', 'telescope', 'plinth', 
   'mouse', 'tripod', 'aardvark' ]
   
TOTAL = 100000
   
def loopbuild():
    for i in range(TOTAL):
        res = []   
        for i in items:
            res.append(i.upper())
            
    return res
   
def mapbuild():
    for i in range(TOTAL):            
        res = list(map(str.upper, items))
        
    return res
   
def compbuild():
    for i in range(TOTAL):
        res = [ s.upper() for s in items ]
        
    return res 
    
   
def genbuild():
    for i in range(TOTAL):
        res = list(s.upper() for s in items)
        
    return res     
     
def main():     
    lb = loopbuild()
    mb = mapbuild()
    cb = compbuild()
    gb = genbuild()























