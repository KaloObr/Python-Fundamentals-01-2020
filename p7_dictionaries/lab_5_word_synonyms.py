from _collections import defaultdict

words_with_synonyms = defaultdict(list)

n = int(input())

for _ in range(n):
    words = input()
    synonym = input()
    words_with_synonyms[words].append(synonym)

for word, synonyms in words_with_synonyms.items():
    print(f'{word} - {", ".join(synonyms)}')