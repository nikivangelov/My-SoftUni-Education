days_count = 1
total_climbed_distance = 5364
reached_everest = False

while days_count <= 5:

    have_rest = input()
    if have_rest == 'END':
        break

    elif have_rest == 'Yes':
        days_count += 1
        if days_count > 5:
            continue
    elif have_rest == 'No':
        days_count += 0
    else:
        break

    climbed_distance = int(input())
    total_climbed_distance += climbed_distance

    if total_climbed_distance >= 8848:
        reached_everest = True
        break
if reached_everest:
    print(f'Goal reached for {days_count} days!')
else:
    print('Failed!')
    print(f'{total_climbed_distance}')


