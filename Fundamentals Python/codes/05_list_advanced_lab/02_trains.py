number_of_wagons = int(input())
train_list = [0] * number_of_wagons
while True:
    command = input()
    if command == 'End':
        break

    data = command.split(' ')
    if data[0] == 'add':
        train_list[-1] += int(data[1])
    if data[0] == 'insert':
        train_list[int(data[1])] += int(data[2])
    if data[0] == 'leave':
        train_list[int(data[1])] -= int(data[2])
print(train_list)