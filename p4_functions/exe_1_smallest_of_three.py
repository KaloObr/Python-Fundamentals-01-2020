def check_smalles_of_three(a, b, c):
    smallest = a

    if b < smallest:
        smallest = b

    if c < smallest:
        smallest = c

    return smallest


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(check_smalles_of_three(num_one, num_two, num_three))
