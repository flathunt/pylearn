# usage: 

# python -i mystuff.py
# >>> from mystuff import *

import importlib
import os
import sys

if sys.platform == 'linux':
    sys.path.append('/home/qa/examples/05 containers')
    sys.path.append('/home/qa/examples/10 modules')
    sys.path.append('/home/qa/examples/11 oo')
else:
    sys.path.append(r'C:\examples\05 containers')
    sys.path.append(r'C:\examples\10 modules')
    sys.path.append(r'C:\examples\11 oo')

from containersdemo \
  import names, numbers, fruit, mixed_fruit, products, new_prod, shapes, instruments, food

msg = 'The cat sat on the mat.'
my_var_names = 'msg', 'names', 'numbers', 'fruit', 'mixed_fruit', 'products', 'newp', 'shapes', 'instruments', 'food'
csvline = 'Fred,33,Artist,12000'

pwd = os.getcwd
cd = os.chdir

def cls():
    os.system('clear' if sys.platform == 'linux' else 'cls')

c = cls    
   
   
def myvars():
    cls()
    for i in my_var_names: 
        print(i, '=', eval('repr(' + i + ')'), end='\n\n')

        
def mystuff():
    print('myvars()', 'pwd()', 'cd()', 'c/cls()', end='\n\n')
    print('importlib.reload(...)')
  
c()

