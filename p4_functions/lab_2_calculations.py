def calculate(operator, num_one, num_two):
    result = 0
    if operator == 'multiply':
        result = num_one * num_two
    elif operator == 'divide':
        result = num_one / num_two
    elif operator == 'add':
        result = num_one + num_two
    elif operator == 'subtract':
        result = num_one - num_two

    return int(result)


input_operator = input()
first_num = int(input())
second_num = int(input())
print(calculate(input_operator, first_num, second_num))
