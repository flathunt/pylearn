catnames = []
while True:
    print('Enter name of cat ' + str(len(catnames) + 1) + ':')
    name = input()
    if name == '':
       break
    catnames = catnames + [name]
print('Cat names are:')
for cat in catnames:
    print(' ' + str(cat))
