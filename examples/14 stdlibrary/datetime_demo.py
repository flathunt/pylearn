#!/usr/local/bin/python

from datetime import date
import time

print(date.today().strftime("%A %d %B %Y"))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1)))
