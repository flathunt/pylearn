#!/usr/local/bin/python

# run as python -Wd warnings_demo.py to get warning

from msgutil import msg, new_msg
import warnings

msg('Harry')
new_msg('Jim')


# For later: move these lines and uncomment...

# warnings.simplefilter('default')
# warnings.filterwarnings('error','.*')




