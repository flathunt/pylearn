# demo...

def testfunc(fn, *args):
    print(fn(*args))
    

testfunc(lambda x,y: x*y, 5, 6)

testfunc(len,'Mary had ... ')
    