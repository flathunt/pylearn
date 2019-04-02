#!/usr/local/bin/python

items = \
    ['elephant', 'telescope', 'plinth',
     'mouse', 'tripod', 'aardvark']

result1 = []
for i in items:
    result1.append(i.upper())
print(result1)


# result2 = list(map(str.upper, items))
# print(result2)


# result3 = [i.upper() for i in items]
# print(result3)
