import inspect

print('importing:', __name__)

def fn1(): print('calling:', inspect.stack()[0][3])
def fn2(): print('calling:', inspect.stack()[0][3])

