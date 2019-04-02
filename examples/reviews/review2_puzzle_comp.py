#!/usr/local/bin/python

# And the answer?

basedata = 'hammer;3;pliers;8;saw;99'
tools = [ int(i) if i.isdecimal() else i for i in basedata.split(';') ]

tooldict = dict(zip(tools[::2], tools[1::2]))

tooldict.update({'gimlet':1, 'saw':28})

letter_set = set('abcde') & set('Fred')

total = sum(tooldict.values()) + len(letter_set)

print(total)


