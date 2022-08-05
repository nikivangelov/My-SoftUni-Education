text = input()
text_dict = {}
for i in range(len(text)):
    key = text[i]
    if key == " ":
        continue
    if key not in text_dict:
        text_dict[key] = 1
    else:
        text_dict[key] += 1

for key, value in text_dict.items():
    print(f"{key} -> {value}")


