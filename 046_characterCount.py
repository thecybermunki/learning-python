# 046 - characterCount.py

message = "Roses are red, but violets aren't blue, they're violet."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

