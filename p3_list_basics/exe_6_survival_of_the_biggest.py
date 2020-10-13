from copy import deepcopy

numbers = list(map(int, input().split()))
nums_to_remove = int(input())

sorted_numbers = deepcopy(numbers)

sorted_numbers.sort(reverse=True)

for i in range(nums_to_remove):
    index = sorted_numbers.pop()
    numbers.remove(index)

print(numbers)
