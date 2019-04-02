#!/usr/local/bin/python

from graph import Graph
 
g1 = Graph("Animal figures")

g1.add('cats', 8)
g1.add('mice', 28)
g1.add('aardvarks', 1)
g1.add('elephants', 67)

g2 = Graph("Product prices")

products = {'CD': 4.99, 'DVD': 9.99, 'Vinyl': 12.99, 'Cassette': 2.99}

for product, price in products.items():
    g2.add(product, int(price + 0.4))


g1.plot()
g2.plot()
