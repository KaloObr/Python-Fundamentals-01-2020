def string_validation(collection):
    for string in collection:
        if not (3 <= len(string) <= 16):
            continue


user_names = input().split(", ")
string_validation(user_names)

