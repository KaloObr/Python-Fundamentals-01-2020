string = input()
temp_ch = ''
new_ch = ''
for i in string:
    if i == temp_ch:
        continue
    else:
        new_ch += i
    temp_ch = i
print(new_ch)
