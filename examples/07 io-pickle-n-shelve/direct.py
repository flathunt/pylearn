#!/usr/local/bin/python

fh = open('../country.txt', 'rb')

index = {}
while True:
    line = fh.readline()
    if not line: break
    fields = line.decode().split(',')
    index[fields[0]] = fh.tell() - len(line) 

while True:    
    key = input('Enter a country: ')  
    if key == '':
        break

    if not key in index:
        print(f"'{key}' not in the file.")
        continue
    
    fh.seek(index[key])
    print(fh.readline().decode(), end="")
