#!/usr/local/bin/python

import os
import sys
import time

path = r'C:\examples' if sys.platform == 'win32' else '/home/qa/examples'

for entry in os.scandir(path):
    if entry.is_file():
        stat = entry.stat()
        mdatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
        print(f'{entry.name:30s} {stat.st_size:5d} {mdatetime}')
