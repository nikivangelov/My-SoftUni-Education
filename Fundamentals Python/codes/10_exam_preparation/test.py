def upper(text: str, start_index: int, end_index: int):
    new_text = ''
    for i in range(len(text)):
        current_letter = text[i]
        if start_index - 1 < i <= end_index - 1:
            current_letter = text[i].upper()
        new_text += current_letter
    return new_text


key = input()
start = int(input())
end = int(input())
print(upper(key, start, end))
