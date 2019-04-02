#!/usr/local/bin/python

msg = 'The cat sat on the mat.'

# search...

search_term = 'sat'
if search_term in msg:
    print('Found', search_term)
   

search_term = 'Th'
if msg.startswith(search_term):
    print('Starts with', search_term)

search_term = 'mat.'
if msg.endswith(search_term):
    print('Ends with', search_term)

# replace...
    
new_msg = msg.replace('cat', 'aardvark')
print(new_msg)






















# names = ['Fred', 'George', 'Harry', 'Eustace', 'Algernon']

# primarys = ('red', 'green', 'blue')

# shapes = {'square', 'triangle', 'circle'}

# instruments = {'trumpet', 'triangle', 'piano'}

# prices = {'CD':4.99, 'DVD':8.99, 'Blu-Ray':12.99}
