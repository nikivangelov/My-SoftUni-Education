coffee_count = 0
while True:
    command = input()
    if command == 'END':
        break

    if command.lower() == 'coding' or command.lower() == 'dog' or command.lower() == 'cat' \
            or command.lower() == 'movie':
        coffee_count += 1
    else:
        continue

    if command.isupper():
        coffee_count += 1

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(f'{coffee_count}')

