#!/usr/local/bin/python

import subprocess
import sys

proc = subprocess.run('slowly',
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.stderr is not None:
    print('ERROR:', proc.stderr.decode(), file=sys.stderr, sep='\n')
    
print('Output:')
print(proc.stdout.decode())
