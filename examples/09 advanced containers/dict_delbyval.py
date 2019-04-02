{v:k for k,v in products.items()}

keys = [ k for k,v in products.items() if v == 2.99 ][0]

del products[key]

keys = [ k for k,v in products.items() if v == 2.99 ]
for key in keys:
    del products[key]
