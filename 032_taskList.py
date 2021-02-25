# 032 - taskList.py

print()

taskList = []
print("what are your tasks for today?")

while True:
    print() 
    print("enter task nr (" + str(len(taskList) + 1) + ") (press enter to leave)")
    task = input()
    if task == '':
        break
    taskList = taskList + [task]

print("your tasks for today are: ")
x = 0 
for task in taskList:
    x = x+1
    print('(' + str(x) + ')' + ' ' + task)

print()
