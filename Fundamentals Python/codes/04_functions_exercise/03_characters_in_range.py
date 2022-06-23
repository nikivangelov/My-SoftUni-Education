def characters_range(start_char, end_char):
    char_list = []
    for i in range(ord(start_char) + 1, ord(end_char)):
        char_list.append(chr(i))
    result = ' '.join(char_list)
    return result


first_char = input()
second_char = input()
print(characters_range(first_char, second_char))
