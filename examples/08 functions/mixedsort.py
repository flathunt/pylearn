#!/usr/local/bin/python

mixed_list = ['zebra', 1001, 'aardvark', 99, 'George', 2.9, 'Fred', 0.3]

mixed_list.sort(key=lambda x:(x,0) if isinstance(x, str) else ('',x))

# mixed_list.sort(key=lambda x:(0,x,0) if isinstance(x, str) else (1,'',x))

print(mixed_list)

