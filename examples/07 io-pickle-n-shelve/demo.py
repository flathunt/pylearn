# !/usr/local/bin/python

# demo very basic file io...


infile_name = 'data.csv'
outfile_name = infile_name.replace('csv', 'tab')

with open(infile_name) as infile, open(outfile_name, 'w') as outfile:
	for line in infile:
		line = line.replace(',', '\t')
		print(line, end='', file=outfile)