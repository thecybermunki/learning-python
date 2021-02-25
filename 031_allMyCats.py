# print 031 - allMyCats.py

print()
catNames = []
while True:
    print("enter the name of cat " + str(len(catNames) + 1) + " or enter nothing to exit")
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print("the cat names are (release drumroll...)")
for name in catNames:
    print('  ' + name)
print()
