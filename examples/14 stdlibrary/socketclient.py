#!/usr/local/bin/python

import os, sys
from socket import *

os.system('clear' if sys.platform == 'linux' else 'cls')

nPortID = 6000

sock = socket(AF_INET, SOCK_STREAM, 0)
sock.connect(("192.168.1.125", nPortID))

print('Connected.')

msg = None
while msg != 'bye':
    msg = input('> ')
    sock.send(msg.encode())
    resp = sock.recv(1024, 0)
    print("Received: ",
          resp.decode())

sock.close()
print('Disconnected.')
