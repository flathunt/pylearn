#!/usr/local/bin/python

not_by_three = [x for x in range(1, 61) if x % 3]

print(not_by_three)

total = sum(not_by_three)

# total = sum(x for x in range(1,61) if x%3)

print('Total:', total)
