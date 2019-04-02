#!/usr/local/bin/python


def logged(fn):
    def inner(*args, **kwargs):
        print('*** calling', fn.__name__, args, kwargs)
        retn = fn(*args, **kwargs)
        print('*** returned', 'from', fn.__name__, '-', retn, end='\n\n')
        return retn

    return inner


@logged
def my_func():
    print('La la la')


@logged
def my_func2(x):
    return [i * x for i in (1, 2, 3)]


my_func()
doubles = my_func2(2)

for i in doubles:
    print(i)
