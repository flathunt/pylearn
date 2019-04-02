#!/usr/local/bin/python

# NOTE: don't try running from /media/sf_examples in VirtualBox VM

import shelve

products = shelve.open('products')
stock = shelve.open('stock')

proddict = {'CD' : 4.99, 'DVD' : 9.99, 'Vinyl' : 12.99, 'Cassette' : 2.99, 'Wax cylinder' : 49.99}

for key in proddict.keys():
    products[key] = proddict[key]

stock['JJ72'] = ('CD', 127)
stock['0898'] = ('CD', 32)
stock['Blackadder'] = ('DVD', 12)

products.close()
stock.close()
