#!/usr/local/bin/python

from subprocess import Popen, PIPE
import sys

#proc = Popen(['ps', '-f'], stdout=PIPE, stderr=PIPE)
proc = Popen('slowly', stdout=PIPE, stderr=PIPE)

(output, errs) = proc.communicate()

if errs:
    print('ERROR:', errs.decode(), file=sys.stderr, sep='\n')
    
print('Output:')
print(output.decode())
