def validate_key_existing(dictionary, key, def_value):
    if key not in dictionary:
        dictionary[key] = def_value


def print_k_v_dictionary(dictionary, template, add_on_dictionary, add_on_template):
    for k, v in dictionary.items():
        print(template.format(k, v))
        for add_v in add_on_dictionary[k]:
            print(add_on_template.format(add_v))


courses_collection = {}
courses_sorted_collection = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    validate_key_existing(courses_collection, course_name, [])
    courses_collection[course_name].append(student_name)

courses_collection = {k: sorted(v) for k, v in courses_collection.items()}
# courses_sorted_collection = {k: len(v) for k, v in courses_collection.items()}
courses_sorted_collection = dict(sorted(({k: len(v) for k, v in courses_collection.items()}).items(), key=lambda x: -x[1]))

print_k_v_dictionary(courses_sorted_collection, "{}: {}", courses_collection, "-- {}")
