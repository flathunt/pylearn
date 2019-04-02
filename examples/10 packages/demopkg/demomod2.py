import inspect

print('importing:', __name__)

def fn21(): print('calling:', inspect.stack()[0][3])
def fn22(): print('calling:', inspect.stack()[0][3])

