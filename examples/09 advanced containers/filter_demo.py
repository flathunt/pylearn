#!/usr/local/bin/python

items = \
  ['elephant', 'telescope', 'plinth', 
   'mouse', 'tripod', 'aardvark']

result1 = []   
for i in items:
    if 'e' in i:
        result1.append(i)
print(result1)


# result2 = list(filter(lambda i: 'e' in i, items))
# print(result2)


# result3 = [i for i in items if 'e' in i]
# print(result3)
