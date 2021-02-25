# 024 - guess-the-number.py

import random

print()
print("hello!")
print("let's play a game!")
print("i think of a number between one and ten and you try to guess the number.")
print("the condition is you only have three guesses.")
print("ready? let's go.")
print()

def takeGuess():
    secret = str(random.randint(1, 11))
    print("take a guess...")
    print()
    for i in range(3):
        print("you have", (3-i), "guesses remaining.")
        guess = input()
        if guess == secret:
            print("correct! you win.")
            print()
            break
        if guess > secret:
            print("you guess too high.")
            print()
        elif guess < secret:
            print("you guess too low")
            print()
        elif guess != secret:
            print("try again")
            print()

takeGuess()

def retryFunc():
    print()
    print("want to go again? <y/n>")
    retry = input()
    if retry == 'y' or 'yes':
        takeGuess()
        print()
    else:
        print("thanks for playing.")
        print()

retryFunc()
