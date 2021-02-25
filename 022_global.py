# 022 - global.py

print()

def foo():
    global apples
    apples = 'local'

apples = 'global'
foo()
print(apples)
print()

############

def bar():
    global oranges
    oranges = 'local'

bar()
oranges = 'global'
print(oranges)

print()
