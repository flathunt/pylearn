import random


lines = int(input('How many lines: '))

for line in range(0, lines):
    lotto = []
    while len(lotto) < 7:
        if len(lotto) < 5:
            lnum = random.randint(1, 50)
        else:
            lnum = random.randint(1, 12)
        if lnum in lotto:
            print(str(lnum) + ' is a duplicate')
            continue
        lotto.append(lnum)
    print(lotto[0:-2], 'Bonus:', lotto[-2:])