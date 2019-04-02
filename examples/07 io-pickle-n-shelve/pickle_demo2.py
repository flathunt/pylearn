#!/usr/local/bin/python

import pickle
import pprint

inp = open('fruitlist.p', 'rb')
fruit_in = pickle.load(inp)
inp.close()

pprint.pprint(fruit_in)
