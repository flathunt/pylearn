#!/usr/local/bin/python

# =====================================================================
# collections...
# =====================================================================

names = ('Mary', 'Fred', 'George', 'Harry', 'Eustace', 'Algernon')
numbers = (2, 15, 7, 0, 12, 6)
fruit = ['apple', 'pear', 'orange', 'kumquat', 'mango']
mixed_fruit = ['Pear', 'apple', 'mango', 'ORANGE', 'kumquat']
products = {'CD': 4.99, 'DVD': 9.99, 'Vinyl': 12.99, 'Cassette': 2.99}
new_prod = {'Blu-ray': 19.99, 'DVD': 4.99}

shapes = {'square', 'circle', 'triangle', 'pentagon'}
instruments = {'piano', 'flute', 'triangle', 'oboe'}
food = ['spam', 'eggs', 'spam', 'spam', 'bacon']

# for simplicity msg is copied...
msg = 'The cat sat on the mat.'


def demo():
    global fruit

    # =====================================================================
    #  min(), max(), sum()
    # =====================================================================

    all(numbers)
    any(numbers)
    min(fruit)
    max(fruit)
    min(numbers)
    max(numbers)
    min(msg)  # will work on strings
    sum(numbers)

    # =====================================================================
    #  creating lists...
    # =====================================================================

    name_list = list(names)
    char_list = list(msg)

    print(name_list, char_list, sep='\n')

    # =====================================================================
    #  add to list...
    # =====================================================================

    fruit += ['lime', 'lemon']

    fruit += 'cherry'

    del fruit[-6:]

    fruit.append('cherry')  # or fruit += 'cherry',

    # =====================================================================
    #  sorts...
    # =====================================================================

    sorted(fruit)
    # gives ['apple', 'cherry', 'kumquat', 'mango', 'orange', 'pear']
    # but fruit still gives original order

    sorted(shapes)
    # gives ['circle', 'pentagon', 'square', 'triangle']

    sorted(shapes, reverse=True)
    # gives ['triangle', 'square', 'pentagon', 'circle']

    sorted(fruit, key=len)
    # gives ['pear', 'mango', 'apple', 'orange', 'cherry', 'kumquat']

    sorted(mixed_fruit)
    # gives ['ORANGE', 'Pear', 'apple', 'kumquat', 'mango']

    sorted(mixed_fruit, key=str.lower)
    # gives ['apple', 'kumquat', 'mango', 'ORANGE', 'Pear']

    fruit.sort()
    print(fruit)
    # gives ['apple', 'cherry', 'kumquat', 'mango', 'orange', 'pear']

    fruit.sort(reverse=True)
    print(fruit)
    # gives ['pear', 'orange', 'mango', 'kumquat', 'cherry', 'apple']

    # =====================================================================
    #  creating sets...
    # =====================================================================

    food_set = set(food)
    print(food_set)
    # gives {'bacon', 'spam', 'eggs'}

    char_set = set(msg)
    print(char_set)
    # gives {'h', 'T', 'a', 'n', '.', 't', 's', 'o', 'm', 'c', ' ', 'e'}

    words = set(msg[:-1].lower().split())
    print(words)
    # gives {'sat', 'cat', 'on', 'mat', 'the'}

    # =====================================================================
    #  Unions intersections etc...
    # =====================================================================

    result = shapes | instruments
    print(result)
    # gives {'piano', 'triangle', 'pentagon', 'flute', 'circle', 'square', 'oboe'}

    result = shapes & instruments
    print(result)
    # gives {'triangle'}

    result = shapes ^ instruments
    print(result)
    # {'piano', 'pentagon', 'flute', 'circle', 'oboe', 'square'}

    result = shapes - instruments
    print(result)
    # gives {'circle', 'square', 'pentagon'}

    unique_foods = set(food)
    print(unique_foods)
    # gives {'eggs', 'bacon', 'spam'}

    # =====================================================================
    # dictionaries...
    # =====================================================================

    demo_dict = dict(balloons=99, trombones=76, bottles=10)
    demo_dict = dict((('balloons', 99), ('trombones', 76), ('bottles', 10)))
    print(demo_dict)

    name_dict = dict(zip(names, numbers))

    name_dict.pop('Fred')

    # name_dict.pop('Jim') # fails
    name_dict.pop('Jim', False)

    name_dict.popitem()

    nd = dict.fromkeys(names, 0)
    print(nd)
    # gives {'Algernon': 0, 'Harry': 0, 'Fred': 0, 'Eustace': 0, 'George': 0}

    products.update(new_prod)
    print(products)
    # gives {'Cassette': 2.99, 'CD': 4.99, 'Vinyl': 12.99, 'Blu-ray': 19.99, 'DVD': 4.99}

    for kv in products.items():
        print(kv)

    for k, v in products.items():
        print(k, v)


if __name__ == '__main__':
    demo()
