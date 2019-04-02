import sys
import re

ports = set()

infile = open('C:\WINDOWS\System32\drivers\etc\services', 'r')
for line in infile:
    valid = re.search(r"(\d+)/(udp|tcp)", line)
    if valid:
        port = int(valid.groups()[0])
        if port > 200:
            break
        ports.add(port)

print(set(range(1, 201)) - ports)
