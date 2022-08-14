import re

numbers = input()
pattern = r"(^|(?<=\s))(\-?)([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.findall(pattern, numbers)
for x in matches:
    print(''.join(x), end=' ')