string_one = input()
string_two = input()
new_word = ''

for index in range(len(string_one)):
    if string_one[index] != string_two[index]:
        letter_one = string_one[index]
        letter_two = string_two[index]
        new_word += letter_two
        print(new_word + string_one[index+1:])
    else:
        new_word += string_one[index]
