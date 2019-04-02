#!/usr/local/bin/python

my_string = 'Fred,33,George,101,Harry,17'

my_list = my_string.split(',')

# my_list = [ int(i) if i.isdigit() else i for i in mystring.split(',') ]

print(my_list)


# For more generic validation...

# re.search(r'^(\+|-)?\d+(\.\d+)?$', num_as_str)
