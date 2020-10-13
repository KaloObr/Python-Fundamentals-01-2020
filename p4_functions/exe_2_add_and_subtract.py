def sum_numbers(num_one, num_two):
    return num_one + num_two


def subtract(sum_nums, num_three):
    return sum_nums - num_three


def add_and_subtract(num_one, num_two, num_three):
    summed = sum_numbers(num_one, num_two)
    result = subtract(summed, num_three)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())


print(add_and_subtract(first_num, second_num, third_num))
