# 041 - method-list-sort.py

print()
foo = ['beta', 'charlie', 'alpha', 'delta']
print("foo:", foo)
bar = ['3', '2', '1', '4']
print("bar:", bar)
spam = ['alpha', 'beta', 'Alpha', 'Beta']
print("spam:", spam)
print()
print("sort")
foo.sort()
bar.sort()
print("foo:", foo)
print("bar:", bar)
print()
print("sort reverse")
foo.sort(reverse=True)
bar.sort(reverse=True)
print("foo:", foo)
print("bar:", bar)
print()
print("sort lower/UPPER")
spam.sort(key=str.lower)
print("spam:", spam)
print()
