#!/usr/local/bin/python

import shelve, sys

products = shelve.open('products')
stock = shelve.open('stock')

print (products[sys.argv[1]])
print (stock[sys.argv[2]])

products.close()
stock.close()
