#!/usr/local/bin/python

sentence = 'The quick brown fox jumps over the lazy dog.'

letters = {char.lower() for char in sentence if char.isalpha()}

print(letters, sorted(letters), len(letters), sep='\n\n')

# ...or...

shells = {user.rstrip().split(':')[-1] for user in open('/etc/passwd')}

for s in sorted(shells):
    print(s)



