start_num = int(input())
end_num = int(input())
ascii_chars = ''

for i in range(start_num, end_num + 1):
    ascii_chars += chr(i) + ' '

print(ascii_chars)

