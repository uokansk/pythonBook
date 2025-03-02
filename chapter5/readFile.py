"""Можно так"""

tasks = open('todos.doc')
for chore in tasks:
    print(chore, end='')
tasks.close()


"""или так"""
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
