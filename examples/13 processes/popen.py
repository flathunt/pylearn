#!/usr/local/bin/python

from subprocess import Popen
import sys

proc = Popen('dir', shell=True)
proc.wait()

print('Ended:', proc.returncode)

