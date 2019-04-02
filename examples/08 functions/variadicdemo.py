#!/usr/local/bin/python

def calc_product(*numbers):
    print(type(numbers), numbers)
    result = numbers[0]
    for i in numbers[1:]:
        result *= i   
    return result
    
print('result:', calc_product(10, 76, 99))


def demodict(**kwargs):
	print(type(kwargs), kwargs)
	
demodict(colour='red', size='medium', weight=10)


def demoargs(*args, **kwargs):
	print(type(args), args, type(kwargs), kwargs)
	
demoargs()
demoargs(99, 'thing', weight=10, colour='red')


    
    
	
    
