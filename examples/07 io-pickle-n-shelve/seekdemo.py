#!/usr/local/bin/python

fo = open('data.csv')

print(fo.tell())
fo.seek(46)
print(fo.tell())

print(fo.read(19))
print(fo.tell())

fo.seek(0)
print(fo.tell())
print(fo.readline())
