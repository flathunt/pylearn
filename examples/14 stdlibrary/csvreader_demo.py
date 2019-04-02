#!/usr/local/bin/python

import csv
import pprint

with open('/etc/passwd', 'r') as csvfile:
    pwreader = csv.reader(csvfile, delimiter=':')
    for row in pwreader:
        print(', '.join(row))

input()

fields = ['user', 'pw', 'uid', 'gid', 'txt', 'home', 'shell']
with open('/etc/passwd', 'r') as csvfile:
    dtreader = csv.DictReader(csvfile,
                              fieldnames=fields, delimiter=':')
    for dtline in dtreader:
        pprint.pprint(dtline)
