# 047 - pretty-character-print.py

print()

import pprint

message = "It was a bright sunny day in February, and the clocks were striking twelve."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

print()
