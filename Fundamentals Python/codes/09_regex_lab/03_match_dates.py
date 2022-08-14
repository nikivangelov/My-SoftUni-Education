import re

given_date = input()
pattern = r'(\d{2})([\/\.\-])([A-Z][a-z]{2})(\2)(\d{4})'
matches = re.findall(pattern, given_date)
for current_date in matches:
    print(f"Day: {current_date[0]}, Month: {current_date[2]}, Year: {current_date[4]}")