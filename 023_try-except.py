# 023 - try-except.py

print()
def foo(x):
    try:
        print("trying 42/" + str(x), ": ", end='')
        print(42 / x)
    except:
        print("error (except)")

foo(7)
foo(3)
foo(2)
foo(1)
foo(0)
print()
