number = int(input())
all_numbers = []
filtered = []

for i in range(number):
    integers = int(input())
    all_numbers.append(integers)

command = input()

if command == "even":
    filtered = [num for num in all_numbers if num % 2 == 0]

elif command == "odd":
    filtered = [num for num in all_numbers if num % 2 != 0]

elif command == "negative":
    filtered = [num for num in all_numbers if num < 0]

elif command == "positive":
    filtered = [num for num in all_numbers if num >= 0]

print(filtered)