import re

phone_number = input()
pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}"
matches = re.findall(pattern, phone_number)
print(', '.join(matches))