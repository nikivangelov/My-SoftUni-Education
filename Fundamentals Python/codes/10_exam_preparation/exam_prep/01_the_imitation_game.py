entry_message = input()
new_message = entry_message
while True:
    command = input().split('|')
    if command[0] == 'Decode':
        break

    elif command[0] == 'Move':
        first_part = new_message[:int(command[1]):]
        second_part = new_message[int(command[1])::]
        new_message = second_part + first_part

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        new_message = new_message[:index] + value + new_message[index:]

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        new_message = new_message.replace(substring, replacement)

print(f"The decrypted message is: {new_message}")