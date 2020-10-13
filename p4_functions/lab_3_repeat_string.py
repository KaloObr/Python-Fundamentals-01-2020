def reversed_string(word, num):
    result = ''
    for i in range(0, num):
        result += word
    return result


string = input()
count = int(input())

print(reversed_string(string, count))
