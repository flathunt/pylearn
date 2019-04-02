from collections import UserDict

class pbvdict(UserDict):

    def pop_by_val(self, value):
        key = [k for k,v in products.items() if v == value][0]
        del products[key]
        return key
        
    def pop_all_by_val(self, value):
        keys = tuple([k for k,v in products.items() if v == value])
        for key in keys:
            del products[key]
        return keys
 
 
pd = {'CD':4.99, 'DVD':9.99, 'Vinyl':12.99, 'Cassette':2.99, 'Book':2.99}
  
products = pbvdict(pd)

print(products)

print(products.pop_by_val(4.99))

print(products)

print(products.pop_all_by_val(2.99))

print(products)

print(products.pop('DVD'))

print(products)


