# if else

print()
print("welcome!")
print("your login credentials are:")
print()
print("username:alice")
print("password:rabbithole")
print()

# input username
print("enter username")
usrName = input()
if usrName != 'alice':
   print()
   print("username not found.")
   print()
else:
    print()
    # input password
    print("enter password")
    usrPassword = input()
    if usrPassword != 'rabbithole':
        print()
        print("wrong password")
        print()
    else:
        print()
        print("login succesful")
        print()

