#!/usr/local/bin/python

fruit_list = [
    {'name': 'lime', 'price': 60},
    {'name': 'apple', 'price': 5},
    {'name': 'pear', 'price': 40},
    {'name': 'cherry', 'price': 100},
    {'name': 'kumquat', 'price': 65},
    {'name': 'mango', 'price': 45},
    {'name': 'banana', 'price': 30}
]


def get_price(fruitdict):
    return fruitdict['price']


fruit_list.sort(key=get_price)

fruit_list.sort(key=lambda fruitdict: fruitdict['price'])
# fruit_list.sort(key=lambda fd: fd['price'])

for fruit in fruit_list:
    print(fruit['name'])


# fruit.sort(key=lambda x: x[::-1])

# values = [1,2,99,0,15]
# inc = 10

# new_values = list(map(lambda a: a+inc, values))

# print(new_values)
