begin_number = int(input())
last_number = int(input())
magic_number = int(input())

combination_count = 0
is_found = False
for first_number in range(begin_number, last_number + 1):
    for second_number in range(begin_number, last_number + 1):
        combination_count += 1
        if magic_number == first_number + second_number:
            print(f'Combination N:{combination_count} ({first_number} + {second_number} = {magic_number})')
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print(f'{combination_count} combinations - neither equals {magic_number}')

