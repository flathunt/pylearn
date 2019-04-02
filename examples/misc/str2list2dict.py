#!/usr/local/bin/python

s = 'fred 33 george 101 harry 17 eustace 29 algernon 43'

nlist = s.split()

ndict1 = dict(zip(nlist[::2],nlist[1::2]))

ndict2 = {k:v for k,v in zip(nlist[::2],nlist[1::2])}

ndict3 = {nlist[i]:nlist[i+1] for i in range(0,len(nlist),2)}

ndict4 = {}
while nlist:
    ndict4[nlist.pop(0)] = nlist.pop(1) # RHS evaluated 1st
    
print(ndict1, ndict2 ,ndict3, ndict4 ,sep='\n')