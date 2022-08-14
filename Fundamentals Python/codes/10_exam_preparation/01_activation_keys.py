def upper_or_lower(command: str, text: str, start_index: int, end_index: int):
    new_text = ''
    for i in range(len(text)):
        current_letter = text[i]
        if start_index - 1 < i <= end_index - 1:
            if command == 'Upper':
                current_letter = text[i].upper()
            elif command == 'Lower':
                current_letter = text[i].lower()
        new_text += current_letter
    return new_text


def slice_command(text: str, start_index: int, end_index: int):
    new_text = ''
    for i in range(len(text)):
        current_letter = text[i]
        if start_index - 1 < i <= end_index - 1:
            continue
        new_text += current_letter
    return new_text


key = input()
while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        break

    elif command[0] == 'Contains':
        if command[1] in key:
            print(f"{key} contains {command[1]}")
        else:
            print("Substring not found!")

    elif command[0] == 'Flip':
        key = upper_or_lower(command[1], key, int(command[2]), int(command[3]))
        print(key)

    elif command[0] == 'Slice':
        key = slice_command(key, int(command[1]), int(command[2]))
        print(key)

print(f"Your activation key is: {key}")