#!/usr/local/bin/python


def gen_eg2():
    items = \
        ['elephant', 'telescope', 'plinth',
         'mouse', 'tripod', 'aardvark']

    return (s for s in items)


def gen_eg():
    items = \
        ['elephant', 'telescope', 'plinth',
         'mouse', 'tripod', 'aardvark']

    for i in items:
        yield i


mygen = gen_eg2()
print(mygen)

for s in gen_eg2():
    print(s)
