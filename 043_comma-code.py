# 043 - comma-code.py

# try using augmented assignments to concatenate strings

print()

# function of comma
def comma(spam):
    spam.insert(-1, 'and')
    for i in range(len(spam[:-2])):
        print(spam[i] + ',', end=' ')
    print((spam[-2]), (spam[-1]))

# insert items to spam
spam = []
while True:
    print('enter item ' + str(len(spam) + 1) + ' (or blank to quit):')
    spamItems = input()
    if spamItems == '':
        break
    spam = spam + [spamItems]

# call function of comma
try:
    comma(spam)
except:
    print('bye')

print()
