#!/usr/local/bin/python

from date_v2 import Date

today = Date(9, 10, 2015)
print(today)  
tomorrow = today + 1
print(tomorrow)

start_date = Date(1, 1, 1970)
start_date += 23
print(start_date)

print('Day is now:', start_date.mday)

start_date.mday = 31

print(start_date)
print(repr(start_date))





