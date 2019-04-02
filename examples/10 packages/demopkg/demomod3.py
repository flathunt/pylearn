import inspect

print('importing:', __name__)

def fn31(): print('calling:', inspect.stack()[0][3])
def fn32(): print('calling:', inspect.stack()[0][3])

