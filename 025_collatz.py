# 025 - collatz.py

print()

def collatz(number):
    while (number != 1):
        if (number % 2 == 0):
            number = (number // 2)
            print(number)
        elif (number % 2 == 1):
            number = (3 * number +1)
            print(number)

print("enter an integer: ")
usrInput = input()

try:
    usrInput = int(usrInput)
except ValueError:
    print()
    print("input error")

collatz(usrInput)
