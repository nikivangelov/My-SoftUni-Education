import re

pattern = r"\b_([A-Za-z0-9]+)\b"
text = input()
regex_text = re.findall(pattern, text)
print(','.join(regex_text))