import random

name = input('What is your name: ')
print('Good Luck ! ', name)
words = ['rainbow', 'computer','python', 'player', 'condition','reverse', 'water', 'board']
word = random.choice(words)
print('Guess the characters')
guesses = ''
turns = 12
while(turns>=1):
    failed = 0
    for char in word:
        if(char in guesses):
            print(char, end=' ')
        else:
            failed += 1
    if(failed == 0):
        print('You Win')
        print('The word is: ', word)
        break
    print()
    guess = input('guess a character: ')
    guesses += guess
    if(guess not in word):
        turns -= 1
        print('Wrong')
        print('You have', + turns, 'more guesses')
        if(turns==0):
            print(word)
            print('You Lose')