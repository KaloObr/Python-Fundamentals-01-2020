def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_k_v_dictionary(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


text = input()
my_dict = {}

for ch in text:
    if ch == " ":
        continue

    validate_key_existing(my_dict, ch)
    my_dict[ch] += 1

print_k_v_dictionary(my_dict, "{} -> {}")

