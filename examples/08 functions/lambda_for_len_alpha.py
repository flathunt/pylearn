#!/usr/local/bin/python

# test = ((3, 'z'), (2, 'z'), (1, 'a'), (1, 'z'), (2, 'a'), (3, 'a'))
# print(sorted(test))

fruit = ['lemon', 'apple', 'pear', 'orange', 'kumquat', 'mango', 'damson']

print(sorted(fruit, key=len))

print(sorted(fruit, key=lambda x: (len(x),x)))

# lambda is equivalent to...

# def thing(x):
#     return (len(x), x)
