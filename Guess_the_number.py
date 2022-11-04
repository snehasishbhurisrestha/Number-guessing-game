from random import *

def computer():
    low = randint(1,200)
    high = randint(300,500)
    number = randint(low,high)
    guess, numberofGuess = 0, 0
    print('Guess a number between',low,'and',high)
    while(guess != number):
        if numberofGuess > 9:
            print('\nYou Loose!\n')
            break
        guess = int(input())
        if guess > number:
            print('Lower number Please!')
            numberofGuess += 1
        elif guess < number:
            print('Higher number Please!')
            numberofGuess += 1
        else:
            print('You guessed the number in',numberofGuess,'attempts!')


def user():
    low = int(input("Enter the lowest value : "))
    high = int(input("Enter the highest value : "))
    number = int(input("Enter the choose value : "))
    guess, numberofGuess = 0, 0
    print('Guess a number between',low,'and',high)
    while(guess != number):
        l, h = False, False
        if numberofGuess > 9:
            print('\nSorry, I Loose!\n')
            break
        guess = randint(low,high)
        print('I guess ',guess)
        if guess > number:
            # print('Lower number Please!')
            l = True
            numberofGuess += 1
            if l == True:
                high = guess
        elif guess < number:
            # print('Higher number Please!')
            h = True
            numberofGuess += 1
            if h == True:
                low = guess
        else:
            print('I guessed the number in',numberofGuess,'attempts!')



# computer()
n = int(input('Press 1 for play with computer else press 2 : '))
if n == 1:
    computer()
elif n == 2:
    user()
else:
    print('Wrong choice!')