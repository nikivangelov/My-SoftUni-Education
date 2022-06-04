height = 5364
day = 1
is_reached = True

while height < 8848:
    if day > 5:
        is_reached = False
    command = input()
    if command == 'End':
        is_reached = False
        break
    else:
        climbed = int(input())
        height += climbed
        if command == 'Yes':
            day += 1
        elif command == 'No':
            continue

if is_reached:
    print(f'Goal reached for {day} days!')
else:
    print('Failed!')
    print(f'{height}')
