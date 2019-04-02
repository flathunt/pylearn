#!/usr/local/bin/python

from time import sleep
import sys

print("Do I have to?", file=sys.stderr, flush=True)
print('line 1', flush=True)
sleep(1)
print('line 2', flush=True)
sleep(1)
print("I'm tired...", file=sys.stderr, flush=True)
print('line 3', flush=True)
sleep(1)
print('line 4', flush=True)
sleep(1)
print("Are we nearly there yet?", file=sys.stderr, flush=True)
print('line 5', flush=True)
sleep(1)
