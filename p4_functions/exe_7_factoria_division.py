def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


def divide_factorials(x, y):

    return fact(x) / fact(y)


first_num = int(input())
second_num = int(input())
print(f"{divide_factorials(first_num,second_num):.2f}")
