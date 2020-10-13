def get_letter_position(letter):
    position_number = 64
    if letter.islower():
        position_number = 96
        return ord(letter) - position_number
    else:
        return ord(letter) - position_number


string = input().split()
total_sum = 0
for char in string:
    # A12b
    f_ch = char[0]
    f_position = get_letter_position(f_ch)
    l_ch = char[-1]
    l_position = get_letter_position(l_ch)
    num = int(char[1:-1])
    current_result = 0

    if f_ch.isupper():
        current_result = num / f_position
    else:
        current_result += num * f_position

    if l_ch.isupper():
        current_result -= l_position
    else:
        current_result += l_position

    total_sum += current_result
print(f'{total_sum:.2f}')
