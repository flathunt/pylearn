#!/usr/local/bin/python

PIN = '0123'
MAX_TRIES = 3

pin_correct = False
tries = 0

while not pin_correct and tries < MAX_TRIES:
    tries += 1
    supplied_pin = input("Enter your PIN:")
    if supplied_pin == PIN:
        pin_correct = True

if pin_correct:
    print("You're in after", tries, "attempt(s)")
else:
    print("You're locked out")
