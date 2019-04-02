#!/usr/local/bin/python

import os, sys
from socket import *

os.system('clear' if sys.platform == 'linux' else 'cls')

nPortID = 6000

sock = socket(AF_INET, SOCK_STREAM, 0)
sock.bind(("", nPortID))
sock.listen(5)

print('Waiting...')

newsock, addr = sock.accept()

print('Connection established.')
sock.close()

responses = (
    b"Hello, I'm Alan\n",
    b'Fine thanks, how are you?\n',
    b"I'm glad to hear it!\n",
    b"...Sorry, you're breaking up, I can't hear you...\n",
    b"...Hello, hello?...\n",
    b"...crackle...\n"
)

idx = 0

while True:
    msg = newsock.recv(1024, 0).decode().rstrip()
    print("Received: ",
          msg)
    if msg == 'bye':
        print('Ended.')
        newsock.send(b'Ended.')
        newsock.close()
        break

    newsock.send(responses[idx])
    idx += 1 if idx < len(responses) - 1 else 0
