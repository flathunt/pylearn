#!/usr/local/bin/python


def getusershell(pgm='bash'):
    for user in open('/etc/passwd'):
        user = user.rstrip()
        username, *others, shell = user.split(':')
        if shell.endswith(pgm):
            newpgm = yield [username, shell]
            if newpgm:
                pgm = newpgm

# def getusershell():
#     return (u.rstrip().split(':')[0:7:6] for u in open('/etc/passwd'))

usergen = getusershell()
user, shell = next(usergen)
print(user, shell)

usergen.send('nologin')
for i in range(3):
    user, shell = next(usergen)
    print(user, shell)





