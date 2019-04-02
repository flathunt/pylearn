#!/usr/local/bin/python

import glob
import sys
import traceback

def dumpfile(filename):
    try:
        with open(filename) as infile:
            for line in infile:
                print(filename, ':', line, end='')
                
    except IOError as e:
        print('\n\nTrapped', e.args)
        
        #error_type, val, tb = sys.exc_info()       # error_type is type(e)
        #print(val)                                 # fuller error msg
        #print("Exception lineno:", tb.tb_lineno)   # line number
        #traceback.print_exc()                      # statement
        #traceback.print_stack() 
        
        sys.exit(e.args[0])

        
def showfiles(pattern):
    for filename in glob.iglob(pattern):
        dumpfile(filename) 

        
def main():        
    showfiles('demo*')
 
 
if __name__ == '__main__':
    main()
    
