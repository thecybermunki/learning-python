# 050 - fantasyGame.py

print()
import sys
import random

inventory = {'arrow': 12, 'gold': 42, 'torch': 1, 'rope': 1, 'dagger': 1}

def displayInventory():
    print()
    itemTotal = 0
    print('Inventory:')
    print('----------')
    for k, v in inventory.items():
            print(k, '(' + str(v) + ')')
            itemTotal += v
    print("Total items: " + str(itemTotal))
    print()

def addInventory():
    print()
    dragonArrow = random.randint(1, 5)
    dragonGold = random.randint(1, 50)
    chanceOfRuby = random.randint(1,2)
    dragonLoot = {'arrow': dragonArrow, 'gold': dragonGold, 'ruby': \
            chanceOfRuby}
    print("You have acquired:")
    print(str(dragonLoot))
    inventory.setdefault('ruby', chanceOfRuby)
    #
    # proper way to add dragonLoot[] to inventory{} ???
    #
    inventory['gold'] = inventory['gold'] + dragonLoot['gold']
    inventory['arrow'] = inventory['arrow'] + dragonLoot['arrow']
    print("Inventory updated.")
    print()

def killDragon():
    print()
    dragonLoot = ['gold', 'ruby']
    chanceOfDeath = random.randint(1, 10)
    if chanceOfDeath < 7:
        addInventory()
    else:
        print("You Died.")
        print()
        sys.exit()
    print()

while True:
    print("You can either <display> inventory or <kill> dragon")
    action = input()
    if action == 'display':
        displayInventory()
    elif action == 'kill':
        killDragon()
    else:
        break

print()
