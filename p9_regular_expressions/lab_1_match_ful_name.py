import re

text = input()
pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

collection = re.findall(pattern, text)
print(" ".join(collection))
