first_char = input()
second_char = input()

start = ord(first_char)
end = ord(second_char)

for i in range(start+1, end):
    print(chr(i), end=' ')

