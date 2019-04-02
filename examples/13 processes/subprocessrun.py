#!/usr/local/bin/python

import subprocess

proc = subprocess.run('slowly')
print('Ended:', proc.returncode)

