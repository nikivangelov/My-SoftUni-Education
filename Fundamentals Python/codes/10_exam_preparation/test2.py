text = input()
start_index = int(input())
end_index = int(input())
new_text = ''
for i in range(len(text)):
    current_letter = text[i]
    if start_index < i <= end_index:
        current_letter = text[i].upper()
    new_text += current_letter

print(new_text)