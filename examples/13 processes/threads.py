#!/usr/local/bin/python

from threading import Thread
import time

def myfunc(*args):
    print("From thread", args)
    time.sleep(2)
   
th1 = Thread(target=myfunc, args='1')
th2 = Thread(target=myfunc, args='2')
th1.start()
th2.start()
print("From main")
th1.join()
th2.join()
