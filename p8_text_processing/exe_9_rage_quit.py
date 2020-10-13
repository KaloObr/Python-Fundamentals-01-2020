string = input().upper()
index = 0
current_symbol = ''
new_string = ''

# abc10
while index < len(string):
    char = string[index]

    if string[index].isdigit():
        is_digit = char

        if index + 1 < len(string) and string[index + 1].isdigit():
            is_digit += string[index+1]
            new_string += current_symbol * int(is_digit)
            current_symbol = ''
            index += 1
        else:
            new_string += current_symbol * int(is_digit)
            current_symbol = ''

    else:
        current_symbol += char

    index += 1

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
