num = int(input())
tank_capacity = 255
current_tank_capacity = 0

for i in range(num):
    current_letters = int(input())

    if current_tank_capacity + current_letters > tank_capacity:
        print('Insufficient capacity!')
        continue
    else:
        current_tank_capacity += current_letters

print(current_tank_capacity)
