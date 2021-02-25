# 034 - list-in-or-not.py

print()

userDatabase = ['alex', 'bob', 'charlie', 'dominique', 'eric', 'franco']
query = input("please enter the name you want to query in the database: ")
if query in userDatabase:
    print("yes,", query, "is in the database")
else:
    print("no results for" + " '" + query + "'.")

print()
