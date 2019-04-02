#!/usr/local/bin/python

products = {'CD': 4.99, 'DVD': 9.99, 'Vinyl': 12.99, 'Cassette': 2.99}

for key, value in products.items():
    print('items()', key, '=', value)

print(products)

while products:
    key, value = products.popitem()
    print('popitem()', key, '=', value)

print(products)




