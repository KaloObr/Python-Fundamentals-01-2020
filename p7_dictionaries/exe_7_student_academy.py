def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_k_v_dictionary(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


number = int(input())
students = {}

for i in range(number):
    student = input()
    grade = float(input())

    validate_key_existing(students, student, [])
    students[student].append(grade)

average_grades = {k: (sum(v) / len(v)) for k, v in students.items() if (sum(v) / len(v) >= 4.5)}

# # Dict comprehension разбит на по прости стъпки
# average_grades = {}
# for k, v in students.items():
#     average_grade = sum(v) / len(v)
#     average_grades[k] = average_grade


# Sorting element
average_grades = dict(sorted(average_grades.items(), key=lambda x: -x[1]))
print_k_v_dictionary(average_grades, "{} -> {:.2f}")

