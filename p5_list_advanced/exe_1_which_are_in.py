words = input().split(', ')
strings = input()
result_list = [word for word in words if word in strings]

print(result_list)
