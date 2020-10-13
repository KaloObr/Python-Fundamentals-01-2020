def register(dictionary, key, def_value):
    if key not in dictionary:
        dictionary[key] = def_value
        print(f"{key} registered {def_value} successfully")
    else:
        print(f"ERROR: already registered with plate number {def_value}")


def print_k_v_dictionary(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


number_of_commands = int(input())
registered_collection = {}

for _ in range(number_of_commands):
    string = input().split()
    name = string[1]
    command = string[0]

    if command == "register":
        plate = string[2]
        register(registered_collection, name, plate)

    if command == "unregister":
        if name in registered_collection:
            registered_collection.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

print_k_v_dictionary(registered_collection, "{} => {}")