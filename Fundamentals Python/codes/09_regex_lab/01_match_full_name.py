import re

name = input()
pattern = r"\b[A-Z][a-z]+\b\s\b[A-Z][a-z]+\b"
match = re.findall(pattern, name)
print(' '.join(match))