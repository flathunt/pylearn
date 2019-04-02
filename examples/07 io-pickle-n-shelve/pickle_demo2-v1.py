#!/usr/local/bin/python

import pickle, sys

inp = open('people.p', 'rb')
people_in = pickle.load(inp)
inp.close()

print (people_in)
