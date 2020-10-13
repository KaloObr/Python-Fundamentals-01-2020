string = input()

for i in range(len(string)):
    if string[i] == ":":
        if i + 1 < len(string) and string[i + 1] != " ":
            print(f":{string[i+1]}")
