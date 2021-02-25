# 054 - pyperclip.py

import pyperclip

print()
pyperclip.copy("hello world!")
usrPaste = input("paste? <y/n>")
if usrPaste == 'y':
    print()
    pyperclip.paste()
    print()
else:
    print()
