import math
numbers = list(map(int,input().split(', ')))

max_values = max(numbers)
group_check = math.ceil(max_values/10)

for group in range(1, group_check+1):
    group_numbers = []
    min_nums = group * 10 - 10
    max_nums = group * 10
    for nums in numbers:
        if min_nums < nums <= max_nums:
            group_numbers.append(nums)

    print(f"Group of {group * 10}'s: {group_numbers}")
