#!/usr/local/bin/python

names = ['Fred', 'George', 'Harry', 'Eustace', 'Algernon']

while names:
    person = names.pop(0)
    print(person)
    if person == 'Eustace':
        break
else:   
    print('No more names')
