number = int(input())
word = input()
temp_list = []
full_list = []

for i in range(number):
    current_string = input()
    full_list.append(current_string)
    if word in current_string:
        temp_list.append(current_string)
    # else:
    #     print("not in the string")
print(full_list)
print(temp_list)
