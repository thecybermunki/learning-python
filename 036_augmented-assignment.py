# 036 - augmented-assignment.py

print()

print("(foo = foo + 1)", "is the same as", "(foo += 1)")
print("(foo = foo - 1)", "is the same as", "(foo -= 1)")
print("(foo = foo * 1)", "is the same as", "(foo *= 1)")
print("(foo = foo / 1)", "is the same as", "(foo /= 1)")
print("(foo = foo % 1)", "is the same as", "(foo %= 1)")

print()
foo = 42
print("foo =", foo)
foo += 1
print("(foo += 1) =", foo)
foo = 42
foo -= 1
print("(foo -= 1) =", foo)
foo = 42
foo *= 1
print("(foo *= 1) =", foo)
foo = 42
foo /= 1
print("(foo /= 1) =", foo)
foo = 42
foo %= 1
print("(foo %= 1) =", foo)

print()
