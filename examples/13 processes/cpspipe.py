#!/usr/local/bin/python

from subprocess import Popen, PIPE
import sys

proc = Popen('slowly', stdout=PIPE, stderr=PIPE)

pipe = proc.stdout
errs = proc.stderr
      
for line in pipe:
    print('OUTPUT:', line.decode(), end='')
         
for line in errs:
    print('ERROR:', line.decode(), file=sys.stderr, end='')  
    
