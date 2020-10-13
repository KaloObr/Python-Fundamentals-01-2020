string = input().split(', ')
number_of_beggers = int(input())
index = 0
total_begger_loot = [[] for _ in range(number_of_beggers)]

while True:
    for i in range(number_of_beggers):
        if index != len(string):
            loot = string[index]
            total_begger_loot[i].append(int(loot))
            index += 1

    if index == len(string):
        break

result = [sum(begger) for begger in total_begger_loot]
print(result)
