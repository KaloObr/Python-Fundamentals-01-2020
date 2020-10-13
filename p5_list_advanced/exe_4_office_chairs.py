number_of_rooms = int(input())
free_charis = 0
successfully_full = 0


for i in range(1, number_of_rooms+1):
    token = input().split()
    chairs = token[0]
    taken_chairs = int(token[1])
    free_charis += len(chairs) - taken_chairs
    if taken_chairs > len(chairs):
        print(f"{taken_chairs - len(chairs)} more chairs needed in room {i}")
        continue

    successfully_full += 1

if successfully_full == number_of_rooms:
    print(f"Game On, {free_charis} free chairs left")


