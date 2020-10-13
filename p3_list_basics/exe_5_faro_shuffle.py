string = input().split()
number_of_splits = int(input())
first_half = []
second_half = []

for shiffle in range(number_of_splits):
    for i in range(len(string)):
        half = len(string) // 2
        if i < half:
            first_half.append(string[i])
        else:
            second_half.append(string[i])

    index = 1

    for i in second_half:
        first_half.insert(index, i)
        index += 2

    string = first_half
    first_half = []
    second_half = []

print(string)
