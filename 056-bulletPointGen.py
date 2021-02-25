#! python3
# 056 - bulletPoint.py - Adds bullet points to the start of each line of text.

print()

# print('Paste a body of text: ')
# import pyperclip
# text = pyperclip.paste()
print('Input a body of text: ')
text = input()

# TODO: seperate lines and add stars.
lines = text.split('. ')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)
print(text)

print()


