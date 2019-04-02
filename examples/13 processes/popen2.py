#!/usr/local/bin/python

from subprocess import Popen
import sys

out = open('output.txt', 'w')

proc = Popen([sys.executable, 'hello.py'], stdout=out)
proc.wait()

print('Ended:', proc.returncode)

out.close()