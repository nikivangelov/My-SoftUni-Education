import re

sentence = input()
pattern = r"(?<= )\b[a-zA-Z0-9][a-zA-Z0-9\.\-_]*@\b[a-zA-Z0-9]+[\.\-][a-zA-Z0-9\.]+[a-zA-Z0-9]\b"
matches = re.findall(pattern, sentence)
for i in range(len(matches)):
    print(matches[i])