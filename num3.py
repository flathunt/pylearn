def count_word3(word): 
    return sum(ord(c) - 96 for c in word)

while True:
    print('Enter word: ')
    word = input()
    if word == '':
       break
    tot = count_word3(word)
    print(tot)
