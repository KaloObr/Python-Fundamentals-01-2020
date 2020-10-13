string = input().split(" ")

word_one = string[0]
word_two = string[1]
min_len = min(len(word_one), len(word_two))

ascii_sum = 0
for char in range(min_len):
    ascii_sum += ord(word_one[char]) * ord(word_two[char])

longest_word = word_one
if len(word_two) > len(word_one):
    longest_word = word_two

for i in range(min_len, len(longest_word)):
    ascii_sum += ord(longest_word[i])

print(ascii_sum)
