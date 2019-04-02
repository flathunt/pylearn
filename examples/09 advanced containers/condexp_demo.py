#!/usr/local/bin/python

numbers = [3, 6, 8, 9, 5, 99, 120, 14, 3]

numbers_oe = ['odd' if x % 2 else 'even' for x in numbers]

print(numbers_oe)

for num, oe in zip(numbers, numbers_oe):
    print(num, oe)

