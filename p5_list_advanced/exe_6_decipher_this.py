def check_digits(string):
    position = 0
    string_numbers = ''

    while string[position].isdigit():
        string_numbers += string[position]
        position += 1

    for i in range(position):
        if i == position - 1:
            string = string.replace(string[0], chr(int(string_numbers)))
        else:
            string = string.replace(string[0], '', 1)

    return string


secret_word = input().split(' ')
result = ''

for word in secret_word:
    word = check_digits(word)

    first_letter = word[1]
    last_letter = word[-1]

    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    result += "".join(word) + " "

print(result)
