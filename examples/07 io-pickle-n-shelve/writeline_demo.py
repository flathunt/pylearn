#!/usr/local/bin/python

mydata = ['line1\n', 'line2\n', 'line3\n']

out = open('data.txt', 'w')

out.writelines(mydata)