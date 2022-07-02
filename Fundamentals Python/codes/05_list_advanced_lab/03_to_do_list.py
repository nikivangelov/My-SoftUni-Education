to_do_list = []
while True:
    command = input()
    if command == "End":
        break
    to_do_list += command.split('-')

print(to_do_list)