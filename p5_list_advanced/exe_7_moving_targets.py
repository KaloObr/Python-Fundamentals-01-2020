def shoot(collection, index, power):
    if index >= len(collection):
        return
    collection[index] -= power

    if collection[index] <= 0:
        collection.pop(index)


def add(collection, index, value):
    if index >= len(collection):
        return print("Invalid placement!")
    collection[index] += value



def strike(collection, index, radius):
    if index + radius >= len(collection[index]):
        return print("Strike missed!")
    for i in collection:
        pass




targets = [int(x) for x in input().split()]
commands = input()

while True:
    if commands == "End":
        break

    token = commands.split()
    action = token[0]
    index = int(token[1])
    value = int(token[2])

    if action == 'Shoot':
        shoot(targets, index, value)

    elif action == 'Add':
        add(targets, index, value)

    elif action == "Stike":
        pass

    commands = input()


