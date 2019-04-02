#!/usr/local/bin/python

# And the answer?

base_data = 'hammer;3;pliers;8;saw;99'
tools = base_data.split(';')

for i in range(1, len(tools), 2):
    tools[i] = int(tools[i])

tool_dict = dict(zip(tools[::2], tools[1::2]))
tool_dict.update({'gimlet': 1, 'saw': 28})

letter_set = set('abcde') & set('Fred')

total = sum(tool_dict.values()) + len(letter_set)

print(total)
