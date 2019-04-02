#!/usr/local/bin/python

import pickle

fruitlist = [
	{ 'name':'lime', 'price':60 },
	{ 'name':'apple', 'price':5 },  
	{ 'name':'pear', 'price':40 },
	{ 'name':'cherry', 'price':100 }, 
	{ 'name':'kumquat', 'price':65 }, 
	{ 'name':'mango',  'price':45 },
	{ 'name':'banana', 'price':30 }
]
    
outp = open('fruitlist.p', 'wb')
pickle.dump(fruitlist, outp, pickle.HIGHEST_PROTOCOL)
outp.close()
