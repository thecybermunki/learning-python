#! python3
# 054 - password-manager.py - An insecure password manager

print()

passwords = {'email': 'nvuaSmc83mc', \
            'blog': 'vmaUfjfa3s', \
            'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python 055-password-manager.py [account] - copy account password' + '\n')
    sys.exit()

account = sys.argv[1] # first cli arg is the account name

if account in passwords:
    print("Password for " + account + " is:")
    print(passwords[account] + '\n')
else:
    print("There is no account named " + account + '\n')

