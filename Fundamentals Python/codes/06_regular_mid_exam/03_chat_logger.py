chat_box = []
while True:
    command_list = input().split(' ')
    if command_list[0] == 'end':
        break

    if command_list[0] == 'Chat':
        chat_box.append(command_list[1])
        # chat_list = " ".join(chat_box)
        # print(chat_list)
    if command_list[0] == 'Delete':
        if command_list[1] in chat_box:
            chat_box.remove(command_list[1])
            # chat_list = " ".join(chat_box)
            # print(chat_list)
    if command_list[0] == 'Edit':
        for char in range(len(chat_box)):
            if chat_box[char] == command_list[1]:
                chat_box[char] = command_list[2]
        # chat_list = " ".join(chat_box)
        # print(chat_list)
    if command_list[0] == 'Pin':
        for char in range(len(chat_box)):
            if chat_box[char] == command_list[1]:
                new_char = chat_box.pop(char)
                chat_box.append(new_char)
        # chat_list = " ".join(chat_box)
        # print(chat_list)
    if command_list[0] == 'Spam':
        for char in range(1, len(command_list)):
            chat_box.append(command_list[char])
        # chat_list = " ".join(chat_box)
        # print(chat_list)
print(*chat_box, sep = "\n")

