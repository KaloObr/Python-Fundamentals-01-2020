number = int(input())
positive_list = []
negative_list = []


for i in range(number):
    ints = int(input())

    if ints >= 0:
        positive_list.append(ints)
    else:
        negative_list.append(ints)

print(positive_list)
print(negative_list)

print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")

