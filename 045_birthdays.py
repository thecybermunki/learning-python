# 045 - birthdays.py

print()

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    print()
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
        print()
    else:
        print('No birthday information for ' + name)
        bday = input('What is their birthday? ')
        birthdays[name] = bday
        print('Birthday database updated.')
        print()

print()
