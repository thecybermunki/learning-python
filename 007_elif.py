# 007 - elif

print()
print("input an integer between 1 and 10:")
usrInput = input()
usrInput = int(usrInput)

if (usrInput > 10) or (usrInput < 1): 
    print()
    print("integer out of bounds.")
    print()
elif usrInput > 5:
    print()
    print("the integer " + str(usrInput) + " is larger than 5.")
    print()
elif usrInput < 5:
    print()
    print("the integer " + str(usrInput) + " is smaller than 5.")
    print()
elif usrInput == 5:
    print()
    print("the integer is equal to 5.")
    print()
