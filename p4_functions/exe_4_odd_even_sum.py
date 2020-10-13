def sum_odd_even(numbers):
    even_sum = 0
    odd_sum = 0

    for i in numbers:
        num = int(i)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


number = str(input())
print(sum_odd_even(number))
