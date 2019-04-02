#!/usr/local/bin/python


def get_bash_users():
    for line in open('/etc/passwd'):
        username, *others, shell = line.rstrip().split(':')
        if shell == '/bin/bash':
            yield username          


for user in get_bash_users():
    print(user)
            
           
"""            
def get_bash_users():
    return \
     (line.split(':')[0] 
       for line in open('/etc/passwd') if '/bin/bash\n' in line)
"""


