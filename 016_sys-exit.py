# 016 - sys.exit()

import sys
print()

while True:
    print("type exit to leave")
    response = input()
    if response == 'exit':
        sys.exit()
    else:
        print()
        print("unknown command")
        print()
