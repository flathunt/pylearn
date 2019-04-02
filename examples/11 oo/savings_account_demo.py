#!/usr/local/bin/python

from account import Account
from savingsaccount import SavingsAccount

account1 = Account(1000.00) 
account1.deposit(550.23)
print(account1.getbalance())

another = SavingsAccount(0, 3)

print('objects:', Account.numCreated)
print("object another is class",
       another.__class__.__name__) 
