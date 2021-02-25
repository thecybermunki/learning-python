# 019 - boring8ball.py

import random
print()

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'a'
    elif answerNumber == 2:
        return 'b'
    elif answerNumber == 3:
        return 'c'
    elif answerNumber == 4:
        return 'd'
    elif answerNumber == 5:
        return 'e'
    elif answerNumber == 6:
        return 'f'
    elif answerNumber == 7:
        return 'g'
    elif answerNumber == 8:
        return 'h'

r = random.randint(1,9)
print(getAnswer(r))
print()
