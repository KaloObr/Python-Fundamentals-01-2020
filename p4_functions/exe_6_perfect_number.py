def check_perfect_number(number):
    current_sum = 0

    for n in range(1, number + 1):
        if current_sum == number:
            return 'We have a perfect number!'
        else:
            current_sum += n

    return "It's not so perfect."


num = int(input())

print(check_perfect_number(num))


