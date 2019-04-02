#!/usr/local/bin/python

countries=[]
for line in open('../country.txt') :
    countries.append(line.split(','))

countries.sort(key=lambda c: (int(c[1])))

for line in countries:
    print(','.join(line), end="")
    
    if 'Atoll' in line[0]: 
        break